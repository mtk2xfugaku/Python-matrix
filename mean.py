# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:30:16 2021

@author: nitin


TODO: write a function to calculate weighted median 
"""
# weighted means but can also be used as normal mean.

# I thin w=[] can be written as w=None then if w: do something
def meanW(seq: list,w=[])->float:
    """
    Weighted arithemtic mean 
    if w = [] then return the arithmetic mean
    else if argument is passed the weighted mean.
    """
    from math import fsum
    if len(w) == 0: # no argument passed
        return fsum(seq)/len(seq)
    elif fsum(w) <= 1.0:
        return fsum(a*b for a,b in zip(seq,w))
    else:
        return fsum(a*b for a,b in zip(seq,w))/fsum(w)

def geomeanW(seq,W=[]):
    """
    weighted geometric mean if W != [] 
    else simple weighted geometric mean.
    """
    from math import fsum, log, exp
    # short circuit evaluation. 
    if len(W) == 0 or fsum(W) <= 1.0:
        s = fsum(log(i) for i in seq)
        return exp(s/len(seq))
    else:
        s = fsum(w*log(i) for w,i in zip(W,seq))
        w_s = fsum(W)
        return exp(s/w_s)
    
def harmonicW(seq,W=[]):
    """
    Weathed harmoic mean of a list of no arguments for 
    weights(W) are given the it will compute the normal
    harmoic mean.
    """
    from math import fsum 
    if len(W) == 0 or fsum(W) <= 1.0:
        denom = fsum(1/i for i in seq)
        return len(seq)/denom
    else:
        w_s = fsum(W)
        s = fsum(w/i for w,i in zip(W,seq))
        return w_s/s

# normal means 

def root_mean(L : list) -> float:
    import math
    """
    root mean squar of a list.
    absent in statistics module.
    """
    store = 0
    for i in L:
        store += i**2
    ans = store/len(L)
    return math.sqrt(ans)


def ArithMean(seq: list)-> float:
    from math import fsum 
    # more accurate floating point summation.
    return fsum(seq)/len(seq)

"""
Alternative ways to compute arithmetic mean

def ArithMean(seq):
    s = 0.0
    for i in seq:
        s += i
    return s/len(seq)

"""
# Geometric mean
def GeoMean(seq):
    from math import fsum, log, exp 
    s = fsum(log(i) for i in seq)
    return exp(s/len(seq))


"""
Alternative ways to compute geometric mean of a list.

Using logarithmetic approximation

def geomean(L):
    # use this one.
    s = 0.0
    n = len(L)
    for i in range(0,n):
        s += math.log(L[i])

    return math.exp(s / n)

Using the standard formula 

def geometric_mean(L : list) -> float:
    
    # this method is not preffered.
    # due to arithmetic overflow error
    power = 1.0/len(L)
    ans = math.pow((mul(L)),power) 
    return ans

Using numpy

def gmean(L):
    try:
        import numpy as np
        a = np.sum(np.log(L))
        return np.exp(a/len(L))
    except ModuleNotFoundError:
        print("numpy module not found !")

"""
# Harmonic mean

def HarmoicMean(seq):
    from math import fsum
    denom = fsum(1/i for i in seq)
    return len(seq)/denom 
"""
Alternatic ways to calculate harmonic mean

def harmonic_mean(L : list) -> float:
    denom = 0 
    for i in L:
        denom += 1/i 
    mean = len(L)/denom
    return mean

"""
