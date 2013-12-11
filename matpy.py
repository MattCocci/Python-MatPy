import numpy as np

# Radnom RV generators
from numpy.random import randn
from numpy.random import rand

# Useful functions
from numpy import linspace


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

# Invert matrix
inv = lambda A: np.linalg.inv(A)


