# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 20:46:58 2016

@author: arnab
"""

import heapq

def findKthlargest(arr, k):
    """
    This can easily be modified to find the median; k = ceil(n/2)
    """
    n = len(arr)
    heap = arr[0:k]
    
    heapq.heapify(heap)
    
    for i in xrange(k, n):
        if arr[i] > heap[0]:
            heapq.heapreplace(heap, arr[i])
    
    print (heap[0])

"""
sort a nearly sorted array:
Source: http://www.geeksforgeeks.org/nearly-sorted-algorithm/
"""

def sortNearlySorted(arr, k):
    
    n = len(arr)
    heap = arr[0:k+1]
    ans = []
    
    # step1 - form a heap with the first k + 1 elements
    heapq.heapify(heap)
    
    # step2 - pop and push the remaining elements
    for i in xrange(k+1, n):
        ans.append(heapq.heapreplace(heap, arr[i]))
    
    # step3 - empty the heap
    while heap:
        ans.append(heapq.heappop(heap))
    
    print (ans)
    

if __name__ == '__main__':
    
    arr = [56, 2, 6, 12, 8, 34, 10, 3, 9]
    k = 3
    
    #sortNearlySorted(arr, k)
    
    findKthlargest(arr, k)
    
    
    