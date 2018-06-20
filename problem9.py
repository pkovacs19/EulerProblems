# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:46:12 2018

@author: pkovacs

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt

def pyTriple(a,b,c):
    return (a**2+b**2)==c**2
    
pyTriple(3,4,5)  

param_space = range(1,1000)  

for i in param_space:
    for j in param_space:
        if i>=j:
            continue
        k=sqrt(i**2 + j**2)
        if i+j+k==1000:
            r=int(i*j*k)
            print(i,j,k,r)
        
        