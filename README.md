# pyGLMHMM

## What Is It?
pyGLMHMM is the pure Python implementation of the GLM-HMM method of this [repository](https://github.com/murthylab/GLMHMM) implemented in MATLAB. It follows the general framework of a [scikit-learn estimator](https://scikit-learn.org/stable/developers/develop.html) while being faithful to the original implementation.

This GLM-HMM model has been developed in ([Calhoun et al., 2019](https://www.nature.com/articles/s41593-019-0533-x)) as a method to infer internal states of an animal based on sensory environment and produced behavior. This technique makes use of a regression method, Generalized Linear Models ([GLMs](https://en.wikipedia.org/wiki/Generalized_linear_model)), that identify a 'filter' that describes how a given sensory cue is integrated over time and then combines with a hidden state model, Hidden Markov Models ([HMMs](https://en.wikipedia.org/wiki/Hidden_Markov_model)), to best predict the acoustic behaviors of the vinegar fly D. melanogaster. The GLM–HMM allows each state to have an associated multinomial GLM to describe the mapping from feedback cues to the probability of emitting a particular type of song. Each state also has a multinomial GLM that produces a mapping from feedback cues to the transition probabilities from the current state to the next state. This allows the probabilities to change from moment to moment in a manner that depends on the sesory feedback that the fly receives and to determine which feedback cues affect the probabilities at each moment. This model was inspired by a previous work that modeled neural activity ([Escola et al., 2011](https://www.mitpressjournals.org/doi/abs/10.1162/NECO_a_00118)), but instead used multinomial categorical outputs to account for the discrete nature of singing behavior.

## Getting Started
### Installation
`pip install pyGLMHMM`

### Instructions on using the pyGLMHMM:

To train a GLM-HMM model, call the function HMMGLMtrain9. This function takes the following form:

HMMGLMtrain9(symb, emit_w, trans_w, stim, analog_emit_w, analog_symb, outfilename, options)

For each trial, we assume the following things:

The trial is of some length T
There are N possible outputs of which only one is emitted per time point
There are M possible states the model can enter
There are K regressors that we are fitting
symb: The output symbols that we are trying to fit. This variable should be a (set) of cells. Each cell represents a trial and contains a vector that is of length T. The elements of the vector should be an integer in the set 0, ..., N-1.

emit_w: The initial weights that predict the emissions at each time point. This should be a matrix of size (number of states, number of emissions - 1, number of regressors) or (M, N-1, K)

trans_w: The initial weights that predict the state transitions at each time point. This should be a matrix of size (number of states, number of states, number of regressors) or (M, M, K)

stim: The stimulus at each time point that we are regressing against. Each cell represents a trial that matches up with the corresponding cell for the symb variable. This matrix should be of size {(number of regressors, number of time points)}, or {(K, T)}

analog_emit_w and analog_symb: Optional. These are for a (somewhat untested) version with gaussian outputs. Use this at your own risk!

## Main Features
![Schematic illustrating the GLM–HMM](https://github.com/aslansd/pyGLMHMM/blob/master/fig/GLM-HMM.jpg)

## Understanding the Main Features

## To Do
### Implementation
- [ ] So far the code was tested and compared with the results of the MATLAB code considering the default options. However, it must be tested and compared with the results of the MATLAB code running with the non-default options too in near future.
- [ ] Since the code was translated from MATLAB, it is not totally [Pythonic](https://docs.python-guide.org/writing/style/), and this somewhat degrades its efficiency. So one major improvement would be re-writting the code in a more Pythonic way.
### Extension
- [ ] The framework presented here can also be extended to include continuous internal states with state-dependent dynamics.
- [ ] In principle, states themselves may operate along multiple timescales that necessitate hierarchical models in which higher-order internal states modulate lower-order internal states. The method presented here can also be extended to include this feature.

## References
1) Calhoun, A. J., Pillow, J. W., & Murthy, M. (2019). Unsupervised identification of the internal states that shape natural behavior. Nature neuroscience, 22(12), 2040-2049.
2) Escola, S., Fontanini, A., Katz, D., & Paninski, L. (2011). Hidden Markov models for the stimulus-response relationships of multistate neural systems. Neural computation, 23(5), 1071-1132.
