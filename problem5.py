# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:01:15 2018

@author: pkovacs

Smallest Multiple:
    
2520 is the smallest number that can be divided by each of the numbers from 1 
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
"""

import numpy as np

a=np.arange(1,21)
i=1
while True:  
    if all(i%a==0):
        print(i)
        break
    i+=1