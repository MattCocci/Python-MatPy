MatPy
======

For those who want their scientific computing terse like MATLAB, but done in Python.

## Motivation
Python is wonderfully general and capable. But when you want to do scientific computing, it's not always clear the best import order to have at the beginning of your module. Maybe your preamble leaves out something important. Maybe you want to import a function directly, but you're concerned about namespace conflicts.  

Plus, sometimes you just want to do stuff quickly (like simulate white noise and plot) without overhead.  You just want to ignore the proper object-oriented way for now, and you don't want to think "To generate a random normal, do I do that from numpy, numpy.random? Or scipy.stats? Or scipy.randn? Or [head smashes into keyboard]"

Finally, maybe you don't want your code to look really ugly and verbose with lots of "np.random", "scipy.stats", "linalg." etc. preceding every operation.

Now compare this to MATLAB. Coding in MATLAB is terse and very useful you need to get stuff done quickly. You don't have to worry about importing different modules, importing functions that might risk namespace conflicts, twenty different ways to do one thing, etc. It's very low cognitive load for simple stuff. 

This repo hopes to bring that over to Python, allowing for quick MATLAB-like coding for those times when you don't need  Python's full object-oriented arsenal. The goal is a __low-overhead scientific computing mode__ that you can enter into for speedy, interactive programming. Then you can worry about proper coding practice once you start to write scripts after some initial experimenting and playing around.

## What This Module Does

So this repo is a Python module which imports useful and commonly-used portions of Python's scientific libraries, then binds them to function names and syntax that are more MATLAB-like (so a simple "randn" for generating random normal variables). 

Plus, it puts everything under one module.  That way, you don't have to worry about messy import statements at the beginning. You can just import the whole shebang with "from matpy import \* ". This module expressly is written with that in mind so you can do that and not worry about namespace conflicts.

## Examples

Here's a taste of how it works. First the super-quick version

    >>> from matpy import *

    >>> a = randn(5)
    >>> a
    array([ 0.98716167,  0.02703619,  1.78872906, -0.1637125 , -1.30310388])
    >>> ascol(a)
    matrix([[ 0.98716167],
            [ 0.02703619],
            [ 1.78872906],
            [-0.1637125 ],
            [-1.30310388]])

    >>> randn(2, 2)
    array([[ 0.27499606, -2.78996343],
           [-0.43519836, -1.98494624]])

    >>> a = randn(2,2)
    >>> size(a)
    (2,2)

    >>> a = eye(2)
    >>> a[1,1] = 2
    >>> inv(a)
    array([[ 1. ,  0. ],
           [ 0. ,  0.5]])



And finally, a quick way to make arrays with some inspiration from R, just because np.array(list) is too long:
    
    >>> c([1,2,3,4,5])
    array([1, 2, 3, 4, 5])

    >>> a = c([[1,2,3], [4,5,6]])
    >>> a
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> size(a)
    (2,3)
    >>> t(a)
    array([[1, 4],
           [2, 5],
           [3, 6]])


    


## Notes for the Nitpicky

Yes, importing everything is bad practice. But sometimes we want to do a quick, one-off simulation at the command line without the bother of endless np.'s floating around. And if I'm really going to replace MATLAB with Python, I better be able to do stuff just as quickly.

So I'm allowing it. And I'm writing this module knowing that I'll want to do it, and so will other people. 

If you really want, you can also do the proper object-oriented thing,

    import numpy as np
    import matplotlib.pyplot as plt
    import matpy as mp

This first brings in NumPy and Pyplot fully (both of which _are_ also nested under matpy, but again, we're shooting for brevity which mp.np.method doesn't satisfy). But this also puts some of the key functionality of interest under the mp heading, like random variable generation and Matlab-like syntax.



