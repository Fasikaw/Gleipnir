"""
Example use of HypSelector with a grouped reactions set of model hypotheses
generated by HypBuilder. In this example, we do the selection
with Nested Sampling via Gleipnir's built-in implenmation of classic Nested
Sampling.

Adapted from the grouped_reactions_example from HypBuilder:
https://github.com/LoLab-VU/HypBuilder/blob/master/grouped_reactions_example.csv

The data used in this example is synthetic data generated from model_0 with the default
parameters defined in the csv file; they are the last 10 timepoints.
"""

import numpy as np
try:
    from pysb.simulator import ScipyOdeSimulator
except ImportError as err:
    raise err
from gleipnir.pysb_utilities import HypSelector


if __name__ == '__main__':

    # The HypBuilder format model csv file.
    model_csv = 'grouped_reactions.csv'
    # The timespan of the simulations.
    tspan = np.linspace(0, 5, 20)
    # Define what ODE solver to use.
    solver = ScipyOdeSimulator
    # Load the data.
    data = np.load("model_0_AB_complex_data.npy")
    # Define the fancy indexer or mask for the time points that the data
    # corresponds to. -- In this case it is the last ten (out of 20) time points.
    data_time_idxs = np.array(list(range(len(tspan))))[10:]
    # Generate the observable data tuple for this observable: (data, data_sd, data_time_idxs)
    obs_data_t = tuple((data,None,data_time_idxs))
    # Generate the dictionary of observable data that is to be used in
    # computing the likelihood. -- Here we are just using the AB_complex
    # observable, which is the amount of A(B=1)%B(A=1).
    observable_data = dict()
    observable_data['AB_complex'] = obs_data_t

    # Build the HypSelector.
    selector = HypSelector(model_csv)
    # Check the number of models that were generated.
    n_models = selector.number_of_models()
    print("Generated {} models from input csv".format(n_models))
    # Append the needed observable to the model files
    obs_line = "Observable(\'AB_complex\',A(B=1)%B(A=1))"
    selector.append_to_models(obs_line)

    # Now let's construct the Nested Samplers for the models.
    # ns_version='built-in' will use Gleipnir's built-in implementation
    # of the classic Nested Sampling algorithm.
    # ns_population_size=100 will set the active population size for the Nested
    # Sampling runs to 100.
    # log_likelihood_type='mse' will use the minus of the Mean Squared Error (mse)
    # as the log_likelihood estimator.
    selector.gen_nested_samplers(tspan, observable_data, solver=solver,
                                 ns_version='built-in',
                                 ns_population_size=100,
                                 log_likelihood_type='mse')

    # Do the Nested Sampling runs. -- The output is a pandas DataFrame.
    # Note that the output is already sorted from highest to lowest log evidence.
    sorted_log_evidences = selector.run_nested_sampling()
    # model_0 is the correct model (i.e., the data comes from a simulaiton of
    # of model_0. However, the order should be: model_0, model_2, and then
    # model_1.
    print("The models and their log_evidence values-sorted:")
    print(sorted_log_evidences)
    print(" ")
    # We can now also look at the Bayes factors which are computed as ratio of
    # evidence values; i.e., evidence_model_column/evidence_model_row
    bayes_factors = selector.bayes_factors()
    print("DataFrame of the Bayes factor matrix:")
    print(bayes_factors)
    print(" ")
    # Let's look at the Bayes factors for model_0; i.e.,
    # evidence_model_0/evidence_other_model
    print("Bayes factors for the model_0 numerator ratios:")
    print(bayes_factors['model_0'])
