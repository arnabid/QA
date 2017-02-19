# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:38:47 2016

@author: arnab
"""

"""
Merge sort: http://quiz.geeksforgeeks.org/merge-sort/
"""

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    
    L = arr[low:mid+1]
    R = arr[mid+1:high+1]
    
    i,j,k = 0,0,low
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    

def mergesort(arr, low, high):
    if low < high:
        mid = low + (high-low)/2
        
        mergesort(arr, low, mid)
        mergesort(arr, mid+1, high)
        
        merge(arr, low, mid, high)

if __name__ == '__main__':
    arr = [2,7,3,1,6,4]
    n = len(arr)
    
    print ("The array before sorting = {} ".format(arr))
    
    mergesort(arr, 0, n-1)
    
    print ("The array after sorting = {} ".format(arr))