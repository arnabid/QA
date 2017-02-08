# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 09:27:39 2016

@author: arnab
"""

"""
median in a stream of integers
"""

import heapq

cm = [float('inf')]
lh, rh = [], []

def findmedian(x):
    if x <= cm[0]:
        if len(lh) <= len(rh):
            heapq.heappush(lh, -x)
        else:
            v = heapq.heapreplace(lh, -x)
            heapq.heappush(rh, -v)
    else:
        if len(rh) <= len(lh):
            heapq.heappush(rh, x)
        else:
            v = heapq.heapreplace(rh, x)
            heapq.heappush(lh, -v)
    
    if len(lh) > len(rh):
        cm[0] = -lh[0]
    elif len(rh) > len(lh):
        cm[0] = rh[0]
    else:
        cm[0] = (-lh[0] + rh[0])/2.0
    
    print (cm[0])
        
    

if __name__ == '__main__':
    arr = map(int, raw_input().strip().split(" "))
    for x in arr:
        findmedian(x)
