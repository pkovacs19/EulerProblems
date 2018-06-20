# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:23:19 2018

@author: pkovacs

Largest Palindrome Product:
    
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


import numpy as np

def testPal(val):
    num=str(val)
    cnt=len(num)
    split=int(cnt/2)
    if cnt%2==0:
        return num[:split]==num[:split-1:-1]
    else:
        return num[:split]==num[:split:-1]
        
a=np.arange(1000)        
b=np.arange(1000)
c=[]

for i in a:
    for j in b:
        c.append(i*j)      
c = np.unique(c)

for i in c[::-1]:
    if testPal(i):
        print(i)
        break
 