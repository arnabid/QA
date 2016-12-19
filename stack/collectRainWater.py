# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:04:01 2016

@author: arnab
"""
"""
Find the amount of water collected on the top of bars
"""

def findwater(bars, n):
    leftmax = [0]
    # leftmax[i] - stores the max bar seen so far to the left of i excluding i

    for i in xrange(1,n):
        leftmax.append(max(leftmax[i-1], bars[i-1]))

    rmax, total = bars[-1], 0

    for i in xrange(n-2,0,-1):
        if leftmax[i] > bars[i] and rmax > bars[i]:
            total += min(leftmax[i], rmax) - bars[i]
        if bars[i] > rmax:
            rmax = bars[i]

    return total


if __name__ == '__main__':
    bars = map(int, raw_input().strip().split(" "))
    n = len(bars)
    
    print (findwater(bars,n))