# pyGLMHMM

## What Is It?
pyGLMHMM is the pure Python implementation of the GLM-HMM model of this [repository](https://github.com/murthylab/GLMHMM) implemented in MATLAB. It follows the general framework of a [scikit-learn estimator](https://scikit-learn.org/stable/developers/develop.html) while being faithful to the original implementation.

This GLM-HMM model has been developed in ([Calhoun et al., 2019](https://www.nature.com/articles/s41593-019-0533-x)) as a method to infer internal states of an animal based on sensory environment and produced behavior. This technique makes use of a regression method, Generalized Linear Models ([GLMs](https://en.wikipedia.org/wiki/Generalized_linear_model)), that identify a 'filter' that describes how a given sensory cue is integrated over time. Then, it combines it with a hidden state model, Hidden Markov Models ([HMMs](https://en.wikipedia.org/wiki/Hidden_Markov_model)), to identify whether the behavior of an animal can be explained by some underlying state. The end goal of this GLM-HMM model is to best predict the acoustic behaviors of the vinegar fly D. melanogaster. The GLM–HMM model allows each state to have an associated multinomial GLM to describe the mapping from feedback cues to the probability of emitting a particular type of song. Each state also has a multinomial GLM that produces a mapping from feedback cues to the transition probabilities from the current state to the next state. This allows the probabilities to change from moment to moment in a manner that depends on the sensory feedback that the fly receives and to determine which feedback cues affect the probabilities at each moment. This model was inspired by a previous work that modeled neural activity ([Escola et al., 2011](https://www.mitpressjournals.org/doi/abs/10.1162/NECO_a_00118)), but instead uses multinomial categorical outputs to account for the discrete nature of singing behavior.

## Getting Started
### Installation
`pip install pyGLMHMM`

### Instructions on using the pyGLMHMM:

num_samples = 5
num_states = 2
num_emissions = 2
num_feedbacks = 3
num_filter_bins = 30
num_steps = 1
filter_offset = 1

output_stim
output_symb
output_symb_analog

For each trial, we assume the following things:

The trial is of some length T.
There are N possible outputs of which only one is emitted per time point.
There are M possible states the model can enter.
There are K regressors that we are fitting.

stim: The stimulus at each time point that we are regressing against. Each cell represents a trial that matches up with the corresponding cell for the symb variable. This matrix should be of size {(number of regressors, number of time points)}, or {(K, T)}.

symb: The output symbols that we are trying to fit. This variable should be a (set) of cells. Each cell represents a trial and contains a vector that is of length T. The elements of the vector should be an integer in the set 0, ..., N-1.

symb_analog: Optional. These are for a (somewhat untested) version with gaussian outputs. Use this at your own risk!

## Main GLM-HMM Method
![Schematic illustrating the GLM–HMM](https://github.com/aslansd/pyGLMHMM/blob/master/fig/GLM-HMM.jpg)

We next determined how the 17 feedback cues and 4 song modes differed across the 3 states of the GLM–HMM. We examined mean feedback cues during each state. We found that in the first state, the male, on average, is closer to the female and moving slowly in her direction; we therefore termed this state the ‘Close’ state. In the second state, the male is, on average, moving toward the female at higher speed while still close, and so we called this the ‘Chasing’ state. In the third state, the male is, on average, farther from the female, moving slowly and oriented away from her, and so we called this the ‘Whatever’ state. However, there was also substantial overlap in the distribution of feedback cues that describe each state, which indicates that the distinction between each state is more than just these descriptors. Another major difference between the states is the song output that dominates—the Close state mostly generates sine song, while the Chasing state mostly generates pulse song and the ‘Whatever’ state mostly no song. However, we note that there is not a simple one-to-one mapping between states and song outputs. All four outputs (no song, Pfast, Pslow and sine) were emitted in all three states, and the probability of observing each output depended on the feedback cues that the animal received at that moment. We compared this model to a GLM–HMM with four states, and it performed nearly as well as the three-state GLM–HMM. We found that three out of the four states corresponded closely to the three-state model, while the fourth state was rarely entered and best matched the ‘Whatever’ state. We conclude that the three-state model is the most parsimonious description of Drosophila song-patterning behavior.

Here, we developed a model (the GLM–HMM) that allows experimenters to identify, in an unsupervised manner, dynamically changing internal states that influence decision-making and, ultimately, behavior. Using this model, we found that during courtship, Drosophila males utilize three distinct sensorimotor strategies (the three states of the model). Each strategy corresponded to a different relationship between inputs (17 feedback cues that affect male singing behavior) and outputs (three types of song and no song). While previous work had revealed that fly feedback cues predict song-patterning decisions, the discovery of distinct state-dependent sensorimotor strategies was only possible with the GLM–HMM.

In conclusion, in comparison to classical descriptions of behavior as fixed action patterns, even instinctive behaviors such as courtship displays are continuously modulated by feedback signals. We also show here that the relationship between feedback signals and behavior is not fixed, but varies continuously as animals switch between strategies. Instead, just as feedback signals vary over time, so too do the algorithms that convert these feedback cues into behavior outputs. Our computational models provide a method for estimating these changing strategies and serve as essential tools for understanding the origins of variability in behavior.

## Minimization Method of EM algorithm
To find the emission and transition matrices of the GLM-HMM model, the [Expectation-Maximization (EM) algorithm](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm) is used. In this algorithm, the negative value of the objective function is minimized. To this end, the [LBFGS](https://en.wikipedia.org/wiki/Limited-memory_BFGS), a popular quasi-Newton method, is used. While [SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html) has a native implementation of LBFGS, its implementation is somewhat different from MATLAB LBFGS implementation in ['minFunc'](https://github.com/murthylab/GLMHMM/tree/master/matlab_code/minFunc) function and has lower performance. As a result, we used the [PyTorch implementation of LBFGS](https://github.com/hjmshi/PyTorch-LBFGS) with the following modifications to make it more similar to the MATLAB implementation and to satisfy the [Wolfe conditions](https://en.wikipedia.org/wiki/Wolfe_conditions):
- The Armijo backtracking line search was directly translated from [here](https://github.com/murthylab/GLMHMM/blob/master/matlab_code/minFunc/ArmijoBacktrack.m).
- The strong Wolfe line search was directly translated from [here](https://github.com/murthylab/GLMHMM/blob/master/matlab_code/minFunc/WolfeLineSearch.m).

The objective function is also converted to a torch neural network module through a [wrapper function](https://github.com/aslansd/pyGLMHMM/blob/master/src/minimizeLBFGS.py).

## To Do
### Implementation
- [ ] So far the code was tested and compared with the results of the MATLAB code considering the default options. However, it must be tested and compared with the results of the MATLAB code running with the non-default options too in near future.
- [ ] Since the code was translated from MATLAB, it is not totally [Pythonic](https://docs.python-guide.org/writing/style/), and this somewhat degrades its efficiency. So one major improvement would be re-writting the code in a more Pythonic way.
### Extension
- [ ] The framework presented here can be extended to include continuous internal states with state-dependent dynamics.
- [ ] In principle, states themselves may operate along multiple timescales that necessitate hierarchical models in which higher-order internal states modulate lower-order internal states. The method presented here can also be extended to include this feature.

## References
1. Calhoun, A. J., Pillow, J. W., & Murthy, M. (2019). Unsupervised identification of the internal states that shape natural behavior. Nature neuroscience, 22(12), 2040-2049.
2. Escola, S., Fontanini, A., Katz, D., & Paninski, L. (2011). Hidden Markov models for the stimulus-response relationships of multistate neural systems. Neural computation, 23(5), 1071-1132.
3. Schmidt, M. (2005). minFunc: Unconstrained Differentiable Multivariate Optimization in Matlab. Software available [here](https://www.cs.ubc.ca/~schmidtm/Software/minFunc.html).
