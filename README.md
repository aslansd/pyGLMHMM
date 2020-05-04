# pyGLMHMM

## What Is It?
pyGLMHMM is the pure Python implementation of the GLM-HMM method of this [GitHub Pages](https://github.com/murthylab/GLMHMM). It follows the general framework of a scikit-learn estimator while being faithful to the original implementation.

The GLM-HMM model has been developed in (Calhoun et al., 2019) as a method to infer internal states of an animal based on sensory environment and produced behavior. This technique makes use of a regression method, Generalized Linear Models (GLMs), that identify a ‘filter’ that describes how a given sensory cue is integrated over time and combines with a hidden state model, Hidden Markov Models (HMMs), to best predict the acoustic behaviors of the vinegar fly D. melanogaster. The GLM–HMM allows each state to have an associated multinomial GLM to describe the mapping from feedback cues to the probability of emitting a particular action (e.g. one type among a few types of a song). Each state also has a multinomial GLM that produces a mapping from feedback cues to the transition probabilities from the current state to the next state. This allows the probabilities to change from moment to moment in a manner that depends on the feedback that the fly receives and to determine which feedback cues affect the probabilities at each moment.

## Getting Started
### Installation
'pip install pyGLMHMM'

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

## Understanding the Main Features

## To Do

## References
