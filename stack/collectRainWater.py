# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:04:01 2016

@author: arnab
"""
"""
Find the amount of water collected on the top of bars
account for holes; -ve values allowed
reference: https://leetcode.com/problems/trapping-rain-water/#/description
"""

def findwater(bars):
    
    # return 0 if empty list
    if not bars:
        return 0

    n = len(bars)
    # leftmax[i] - the max bar to the left of bar i including i
    leftmax = [bars[0]]

    for i in xrange(1,n-1):
        leftmax.append(max(leftmax[i-1], bars[i]))

    rmax, total = bars[-1], 0

    for i in xrange(n-2,0,-1):
        if leftmax[i] > bars[i] and rmax > bars[i]:
            total += min(leftmax[i], rmax) - bars[i]
        if bars[i] > rmax:
            rmax = bars[i]
    
    if bars[0] < 0:
        total += abs(bars[0])
    
    if bars[-1] < 0:
        total += abs(bars[-1])

    return total


if __name__ == '__main__':
    bars = map(int, raw_input().strip().split(" "))
    
    print (findwater(bars))