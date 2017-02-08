# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:22:16 2016

@author: H138576
"""

"""
merge k sorted arrays
"""
import heapq

def merge(arr, k):
    # form a heap with k elements; first item from each of the k lists
    # each item in the heap = (value, (a,b))
    # value = element in the ath list and at the bth index
    h = []
    ans = []
    for i in range(k):
        if arr[i]:
            heapq.heappush(h, (arr[i][0], (i,0)))
        else:
            heapq.heappush(h, (float('inf'), (i,0)))
    
    while h[0][0] != float('inf'):
        value, (l,index) = heapq.heappop(h)
        ans.append(value)
        if (index+1) < len(arr[l]):
            heapq.heappush(h, (arr[l][index+1],(l,index+1)))
        else:
            heapq.heappush(h, (float('inf'),(l,index+1)))
    return (ans)

if __name__ == '__main__':
    arr = [[1,2,3,10], [4,7,9,21,25], [5]]
    k = len(arr)  # number of lists
    
    print (merge(arr, k))
