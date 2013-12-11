MatPy
======

For those who want their scientific computing terse like MATLAB, but done in Python.

## Motivation
Python is wonderfully general and capable. But when you want to do scientific computing, it's not always clear the best import order to have at the beginning of your module. Maybe your preamble leaves out something important. Maybe you can import directly a function directly, not worrying about namespace conflicts.  

Plus, sometimes you just want to do stuff quickly (like simulate white noise and plot) without overhead.  You just want to ignore the proper object-oriented way for now, and you don't want to think "To generate a random normal, do I do that from numpy, numpy.random? Or scipy.stats? Or scipy.randn? Or [head smashes into keyboard]"

Finally, maybe you don't want your code to look really ugly and verbose with lots of "np.random", "scipy.stats", "linalg." etc. preceding every operation.

Now compare this to MATLAB. Coding in MATLAB is wonderfully terse when you need to get stuff done quickly. You don't have to worry about importing different modules, importing everything and thereby risking namespace conflicts, twenty different ways to do one thing, etc. It's very low cognitive load for simple stuff. 

This repo hopes to bring that over to Python, allowing for quick MATLAB-like coding for those times when you don't need  Python's full object-oriented arsenal.

## What This Module Does

So this repo is a Python module which imports useful and commonly-used portions of Python's scientific libraries, then binds them to function names that are more MATLAB-like (like a simple "randn" for generating random normal variables). 

Plus, it puts everything under one module.  That way, you don't have to worry about messy import statements at the beginning. And if you just want to import the whole shebang with "from matpy import \* ", go for it. This is written so you can do that and not worry about namespace conflicts.

## Examples

Here's a taste of how it works. First the super-quick version

    >>> from matpy import *

    >>> randn(5)
    array([-0.42073853,  1.90156021, -0.78803865,  0.78138721, -0.69243448])

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


And finally, some inspiration from R, just because np.array(list) is too long:
    
    >>> c([1,2,3,4,5])
    array([1, 2, 3, 4, 5])
    


## Notes for the Nitpicky

Yes, importing everything is bad practice. But sometimes we want to do a quick, one-off simulation at the command line without bother with endless "np." If I'm going to replace MATLAB with Python, I better be able to do stuff quickly like that.

So I'm allowing it. And I'm writing this module knowing that I'll want to do it, and so will other people. 

If you really want, you can also do the proper object-oriented thing,

    import matpy as mp

and get all this functionality under one heading



