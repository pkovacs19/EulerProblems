# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:29:21 2018

@author: pkovacs

Sum Square Difference 

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""

import numpy as np

a=np.arange(1,101)
a.sum()**2-sum(a**2)
