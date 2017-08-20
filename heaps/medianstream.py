# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 09:27:39 2016

@author: arnab
"""

"""
median of a stream of integers
reference: https://www.youtube.com/watch?v=VmogG01IjYc

maintain 2 heaps: lh(max heap); rh(min heap)
add number to either heaps based on value
rebalance heaps if necessary; size of heaps differs by atmost 1
return median based on size of heaps
"""

import heapq
lh, rh = [], []

def findmedian(x):
    # add x to the lower or higher heap
    if len(lh) == 0 or x < -lh[0]:
        heapq.heappush(lh, -x)
    else:
        heapq.heappush(rh, x)
    
    # rebalance if necessary
    if len(lh) - len(rh) >= 2:
        number = -heapq.heappop(lh)
        heapq.heappush(rh, number)
    elif len(rh) - len(lh) >= 2:
        number = heapq.heappop(rh)
        heapq.heappush(lh, -number)
    
    # return median
    if len(lh) > len(rh):
        return -lh[0]
    elif len(rh) > len(lh):
        return rh[0]
    else:
        return (-lh[0] + rh[0]) / float(2)

if __name__ == '__main__':
    arr = map(int, raw_input().strip().split(" "))
    for x in arr:
        print (findmedian(x)),
