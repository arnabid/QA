# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:02:34 2017

@author: arnab
"""

"""
N light bulbs are connected by a wire. Each bulb has a switch associated with it,
however due to faulty wiring, a switch also changes the state of all the bulbs
to the right of current bulb. Given an initial state of all bulbs,
find the minimum number of switches you have to press to turn on all the bulbs.
You can press the same switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.

Input : [0 1 0 1]
Return : 4

Explanation :
	press switch 0 : [1 0 1 0]
	press switch 1 : [1 1 0 1]
	press switch 2 : [1 1 1 0]
	press switch 3 : [1 1 1 1]
"""

def bulbs(arr):
    n = len(arr)
    flips = 0
    for i in xrange(n):
        if not (flips % 2 ^ arr[i]):
            flips += 1
        arr[i] = 1
    return arr, flips

if __name__ == '__main__':
    arr = [0,1,0,1]
    print (bulbs(arr))