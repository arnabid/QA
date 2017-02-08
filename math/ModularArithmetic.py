# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:27:51 2016

@author: arnab
"""
import random

if __name__ == '__main__':
    x = random.randint(2,10)
    n = random.randint(1,9)
    m = random.randint(1,10)
    
    print (x,n,m)
    res1 = (((x ** (n+1)) - 1) / (x-1)) % m
    
    res2 = None
    if x%m == 1:
        res2 = (n+1)%m
    else:
        res2 = ((((x%m) ** (n+1)) - 1) / ((x%m) - 1)) % m
    
    print ("Results: ", res1, res2)

    
