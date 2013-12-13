import numpy as np
import matplotlib.pyplot as plt

# Random RV generators
from numpy.random import randn
from numpy.random import rand

# NaN stuff
from numpy import nan, isnan

# Import useful vectorized functions
from numpy import linspace, exp, cos, sin, log, \
        mean, var, std, cumsum, cumprod, dot

# Import matrix operations
from numpy.linalg import inv, det, solve, eigvals

# Import probability distributions
from scipy.stats import beta, binom, chi2, gamma, \
        invgamma, lognorm, norm, uniform 

# Import plotting
from matplotlib.pyplot import plot, xlabel, ylabel, \
        show, axis, subplot, title, figure, grid, \
        hist, text


# c() function like in R to concatenate and make an array
c = lambda seq: np.array(seq)

# Matlab-like ones function
def ones(r, c=1):
    if c == 1:
        return np.ones(r)
    else:
        return np.ones((r, c))

# Matlab-like zeros function
def zeros(r, c=1):
    if c == 1:
        return np.zeros(r)
    else:
        return np.zeros((r, c))

# Matlab-like eye function
eye = lambda n: np.eye(n)

# Size of matrix/array
size = lambda array: array.shape

# Induce an array to be a column matrix
ascol = lambda x: np.transpose(np.matrix(x))
    
# Transpose
t = lambda x: np.transpose(x)

# Convert 0, 1 array to logical
lgcl = lambda x: np.array(x, dtype=bool)






