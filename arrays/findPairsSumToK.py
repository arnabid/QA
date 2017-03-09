# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:07:04 2017

@author: arnab
"""

"""
find the number of pairs of elements that sum to a given value
array might have values with repeated elements
"""

from collections import Counter

def sol(arr, k):
    c = Counter(arr)
    
    result = 0
    for x in arr:
        if (k - x) in c:
            result += c[k-x]
        
        if k - x == x:
            result -= 1
    
    return result/2
            

if __name__ == '__main__':
    arr = [3,5,1,7,6,4]
    k = 10
    print (sol(arr, k))