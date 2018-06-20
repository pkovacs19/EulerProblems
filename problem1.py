# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 09:46:25 2018

@author: pkovacs

Multiples of 3 and 5:
    
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 
    3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
"""

import numpy as np
import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def sum_multi_3_5(size):
    a = np.arange(1,1000)   
    sum([i for i in a if (i%3==0 or i%5==0)])

soln = wrapper(sum_multi_3_5,1000)
timeit.timeit(soln,number=1000)

