MatPy
======

For those who want their scientific computing terse like MATLAB, but done in Python.

## Motivation
Python is wonderfully general and capable. But when you want to do scientific computing, it's not always clear the best import order to have at the beginning of your model (or where the statistics and probability distribution functions should be coming from.) On top of that, things can look really ugly and quote verbose if you have lots of "np." and "scipy.stats." preceding everything.

On the other hand, coding in MATLAB is wonderfully terse when you need to get stuff done quickly. You don't have to worry about importing different modules, importing everything and risking namespace conflicts, etc. 

## What This Module Does

So this repo is a python module which gets the import order correct and puts everything under one module. Plus, it uses Matlab names for like "randn" for generating random normal variables. That way, you don't have to worry about the import statements. Plus, it's written so that if you just want to import the whole shebang with "from matpy import \*", you can do it and not worry about namespace conflicts.

## Examples

Here's a taste of how it works. First the super-quick version

    >>> from matpy import *
    >>>
    >>> randn(5)
    array([-0.42073853,  1.90156021, -0.78803865,  0.78138721, -0.69243448])
    >>>
    >>> randn(2, 2)
    array([[ 0.27499606, -2.78996343],
           [-0.43519836, -1.98494624]])
    >>>
    >>> a = randn(2,2)
    >>> size(a)
    (2,2)
    >>>
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



