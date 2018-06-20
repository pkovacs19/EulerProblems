# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:32:33 2018

@author: pkovacs

Prime Factors:
    
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#! unfinished

import numpy as np
a=np.arange(2,13195+1)
for i in a:
    print(i)
    a=a[a%i!=0]


a[a%2!=0]   
