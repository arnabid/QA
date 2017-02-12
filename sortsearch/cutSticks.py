# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 22:14:45 2016

@author: arnab
"""

"""
cut the sticks
Hackerrank: https://www.hackerrank.com/challenges/cut-the-sticks
"""

if __name__ == '__main__':   
    arr = map(int,raw_input().strip().split(' '))
    arr.sort()
    n = len(arr)
    mn, i = 0, 0
    while i < n:
        if arr[i] > mn:
            print (n-i)
            mn = arr[i]
        i += 1
