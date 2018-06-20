# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:46:55 2018

@author: pkovacs

10001st Prime Number

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10 001st prime number?
"""

import numpy as np

def findPrimes(num):
    a=np.array([2])
    i=3
    while len(a)<num:
        if all(i%a!=0):
            a=np.append(a,i)
        i+=1
    return a

res = findPrimes(10001)

print(res[-1])