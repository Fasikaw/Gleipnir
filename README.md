# Gleipnir

<p align="center">
  <img width="100" height="100" src="./images/gleipnir_logo_2.png">
</p>


Gleipnir is a python toolkit that provides an easy to use interface for Nested Sampling that is similar to the calibration tools [PyDREAM](https://github.com/LoLab-VU/PyDREAM) and [SimplePSO](https://github.com/LoLab-VU/ParticleSwarmOptimization). Gleipnir has a built-in implementation of the classic Nested Sampling algorithm, and the toolkit provides a common interface to the Nested Sampling implementations MultiNest, PolyChord, and DNest4. Gleipnir also has some PySB model-specific utilities, including nestedsample_it/NestedSampleIt and HypSelector (read more under the PySB Utilities section).

Through Nested Sampling simulations, Gleipnir can be used to compute the Bayesian evidence (or marginal likelihood) of models. The Bayesian evidence can in turn be used for model selection; i.e., users can select between competing models and determine which one is best supported by the data. And as a side-effect of the evidence calculation, estimates of the posterior distributions of the parameters can also be generated; therefore, Gleipnir can also be used for Bayesian model calibration.

### What is Nested Sampling?

Nested Sampling is a numerical integration scheme for estimating Bayesian evidence (i.e., the normalization factor or denominator in Bayes formula for probability distributions) integrals.

In particular, Nested Sampling was
designed to handle cases where the evidence integral is high-dimensional and the likelihood is exponentially localized in the probability mass of the prior distribution of the sampled dimensions. In the Nested Sampling approach, the evidence is first converted from a (possibly) multi-dimensional integral into a one-dimensional integral taken over a mapping of the likelihood function to elements of the unit prior probability mass (X). In principle, this is achieved by using a top-down
approach in which sample points are drawn according to the prior distribution, and the unit prior probability is subdivided
into equal fractional elements from X = 1 down to X = 0 and
mapped to the likelihood function, L(X), via a likelihood sorting routine.

The Nested Sampling method was originally developed by John Skilling; see the following references:
  1. Skilling, John. "Nested sampling." AIP Conference Proceedings. Vol.
    735. No. 1. AIP, 2004.
  2. Skilling, John. "Nested sampling for general Bayesian computation."
    Bayesian analysis 1.4 (2006): 833-859.
  3. Skilling, John. "Nested sampling’s convergence." AIP Conference
    Proceedings. Vol. 1193. No. 1. AIP, 2009.

------

# Install

| **! Warning** |
| :--- |
|  Gleipnir is still under heavy development and may rapidly change. |

## Gleipnir run dependencies
Gleipnir has the following core dependencies:
   * NumPy - http://www.numpy.org/
   * SciPy - https://www.scipy.org/
   * pandas - https://pandas.pydata.org/

### To use PolyChord
   * pypolychord - https://github.com/PolyChord/PolyChordLite

### To use MultiNest
   * PyMultiNest - https://github.com/JohannesBuchner/PyMultiNest
   * MultiNest -  https://github.com/JohannesBuchner/MultiNest

### To use DNest4
   * DNest4 - https://github.com/eggplantbren/DNest4

### To use PySB models
   * PySB - http://pysb.org/

### To run the Jupyter notebooks
   * Jupyter - https://jupyter.org/   

### Recommended packages for plotting
   * matplotlib - https://matplotlib.org/
   * seaborn - https://seaborn.pydata.org/        

### To use the HypSelector tool (see the PySB Utilities section)
   * HypBuilder - https://github.com/LoLab-VU/HypBuilder

Gleipnir is compatible with Python 3.6

The following section describes the process for setting up the dependencies using a conda environment (https://conda.io/en/latest/).

## Setup and install using conda

First, clone or download the GitHub repo
```
git clone https://github.com/LoLab-VU/Gleipnir.git
```
Then create a new conda environment for gleipnir using the environment.yml file
(which includes the core dependencies):
```
conda env create -f Gleipnir/environment.yml
```
Activate the environment
```
conda activate gleipnir
```
Then from the Gleipnir directory/folder you can install gleipnir into the environment using the setup.py script:
```
python setup.py install
```
## Optional package installation

### To run pysb models (and use gleipnir.pysb_utilities):
```
conda install -c alubbock pysb
```

### To run Jupyter notebooks:
```
conda install jupyter
```

### Recommended plotting packages:
```
conda install matplotlib seaborn
```

### PolyChord
If you want to use the PolyChordNestedSampling object for the Nested Sampling runs then download, build, and install pypolychord following instructions in the README at:

https://github.com/PolyChord/PolyChordLite

Notes:
 * Installs into your .local/lib python site-packages.
 * Requires gfortran (f77 compiler) and lipopenmpi-dev (development libraries for MPI) to build the code.

### MultiNest
If you want to use the MultiNestNestedSampling object for Nested Sampling download, build, and install PyMultiNest and MultiNest following the instructions at:
http://johannesbuchner.github.io/PyMultiNest/install.html

### DNest4
If you want use the DNest4NestedSampling object for Nested Sampling then download,
build, and install DNest4 and its Python bindings following the instructions in the README at:
https://github.com/eggplantbren/DNest4

Notes:
 * Requires a c++ compiler with c++11 standard libraries.
 * Requires Cython and numba for python bindings to compile and install

### HypBuilder
If you want use the HypSelector tool from gleipnir.pysb_utilities then you
need to have HypBuilder:
```
git clone https://github.com/LoLab-VU/HypBuilder
```
Then you will need to add the HypBuilder directory/folder to your PYTHONPATH
environment variable to be able to import from HypBuilder.

------

# Documentation and Usage

Checkout the Jupyter Notebook (more in the pipeline):
 1. [Intro to Nested Sampling with Gleipnir](./jupyter_notebooks/Intro_to_Nested_Sampling_with_Gleipnir.ipynb)
 2. [HypSelector Example](./jupyter_notebooks/HypSelector_example.ipynb)
 3. [ModelSelector Example](./jupyter_notebooks/ModelSelector_example.ipynb)

Also checkout the [examples](./examples) to see example scripts that show how to setup Nested Sampling runs using Gleipnir.



------

# PySB Utilities

## nestedsample_it
nestedsample_it is a utility that helps generate a Nested Sampling run script or NestedSampling objects for a PySB model.

### Commmand line use
nestedsample_it can be used as a command line utility to generate a template Nested Sampling run script for a PySB model. nestedsample_it reads the model file, imports and pulls out all the kinetic parameters, and then writes out a run_NS script for that model. nestedsample_it currently writes out a run script for classic Nested Sampling via Gleipnir, so you'll need to modify it to use one of the other Nested Samplers (MultiNest, PolyChord, or DNest4). And you will need to edit the run script to load any data and modify the loglikelihood function, but nestedsample_it should give you a good starting point.

Run nestedsample_it from the command line with following format:
```
python -m glepnir.pysb_utilities.nestedsample_it model.py output_path
```      
where output_path is the directory/folder location where you want the generated script
to be saved.

The command line version of nestedsample_it also has support for a limited set of #NESTEDSAMPLE_IT directives which can be added to model files. The current directives are:
  * #NESTEDSAMPLE_IT prior [param_name, param_index] [norm, uniform]  
    * Specify the type of prior to assign to a parameter. The parameter can either be specified by its name or its index (in model.parameters). The priors that can be assigned are either norm or uniform; note that uniform is the default for all parameters.  
  * #NESTEDSAMPLE_IT no-sample [param_name, param_index]
     * Specify a fixed parameter (i.e., not to included in sampling). The parameter can either be specified by its name or its index (in model.parameters).          


### Progammatic use via the NestedSampleIt class
The nestedsample_it utility can be used progammatically via the NestedSampleIt
class. It's importable from the pysb_utilities module:
```python
from gleipnir.pysb_utilities import NestedSampleIt
```
The NestedSampleIt class can build an instance of a NestedSampling object.  
 Here's a minimal example:
```python
from my_pysb_model import model as my_model
from gleipnir.pysb_utilities import NestedSampleIt
import numpy as np

timespan = np.linspace(0., 10., 10)
data = np.load('my_data.npy')
data_sd = np.load('my_data_sd.npy')
observable_data = dict()
time_idxs = list(range(len(timespan)))
observable_data['my_observable'] = (data, data_sd, time_idxs)
# Initialize the NestedSampleIt instance with the model details.
sample_it = NestedSampleIt(my_model, observable_data, timespan)
# Now build the NestedSampling object. -- All inputs are
# optional keyword arguments.
nested_sampler = sample_it(ns_version='gleipnir-classic'
                           ns_population_size=100,
                           ns_kwargs=dict(),
                           log_likelihood_type='logpdf')
# Then you can run the nested sampler.
log_evidence, log_evidence_error = nested_sampler.run()
```

NestedSampleIt constructs the NestedSampling object to sample all of a model's kinetic rate parameters. It assumes that the priors are uniform with size 4 orders of magnitude and centered on the values defined in the model. Currently there is no way to change the parameters that are sampled, or the priors used by NestedSampleIt; if these are features you would like to have then please open an [issue](https://github.com/LoLab-VU/Gleipnir/issues) and let me know.

In addition, NestedSampleIt crrently has three pre-defined loglikelihood functions with different estimators. They can be specified with the keyword parameter log_likelihood_type:
```python
# Now build the NestedSampling object.
nested_sampler = sample_it(log_likelihood_type='logpdf')
```
The options are
  * 'logpdf'=>Compute the loglikelihood using the
normal distribution estimator
  * 'mse'=>Compute the loglikelihood using the
negative mean squared error estimator
  * 'sse'=>Compute the loglikelihood using
the negative sum of squared errors estimator.
The default is 'logpdf'.
Each of these functions computes the loglikelihood estimate using the timecourse output of a model simulation for each observable defined in the `observable_data` dictionary.
If you want to use a different or more complicated likelihood function with NestedSampleIt then you'll need to subclass it and override one of the existing loglikelihood functions.  

## HypSelector

HypSelector is a tool for hypothesis selection using [HypBuilder](https://github.com/LoLab-VU/HypBuilder) and Nested Sampling-based model selection. Models embodying different hypotheses (e.g., optional reactions) can be defined using the HypBuilder csv syntax. HypSelector then allows users to easily compare all the hypothetical model variants generated by HypBuilder by performing Nested Sampling to compute their evidences and thereby do model selection; HypSelector also provides functionality to estimate Bayes factors from the evidence estimates, as well as estimators for the Akaike, Bayesian, and Deviance information criteria computed from the Nested Sampling outputs. See the [grouped reactions example](./examples/HypSelector/grouped_reactions) or the [HypSelector Example Jupyter Notebook](./jupyter_notebooks/HypSelector_example.ipynb) to see example usage of HypSelector.

## ModelSelector

Similar to HypSelector, ModelSelector is a tool for PySB model selection using Nested Sampling-based model selection. ModelSelector allows users to easily compare model variants written in PySB and see which one may best explain a dataset by performing Nested Sampling to compute their evidences and thereby do model selection; ModelSelector also provides functionality to estimate Bayes factors from the evidence estimates, as well as estimators for the Akaike, Bayesian, and Deviance information criteria computed from the Nested Sampling outputs. See the [ModelSelector Example Jupyter Notebook](./jupyter_notebooks/ModelSelector_example.ipynb) to see example usage of ModelSelector.
