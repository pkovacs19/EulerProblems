# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 16:31:38 2018

@author: pkovacs

Summation of Primes:
    
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import numpy as np

def findPrimes(num):
    a=np.array([2])
    for i in range(3,num):
        if all(i%a!=0):
            a=np.append(a,i)
    return a



res = findPrimes(int(2e6))
print(res.sum())