# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 00:42:36 2016

@author: arnab
"""
"""
Find the number of inversions in the array: a[i] > a[j], i < j
"""

ans = [0]

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
            ans[0] += n1 - i # add the number of inversions
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
        mid = (low+high) // 2
        
        mergesort(arr, low, mid)
        mergesort(arr, mid+1, high)
        
        merge(arr, low, mid, high)

if __name__ == '__main__':
    n = int(raw_input())
    a = map(int, raw_input().strip().split(" "))
    mergesort(a, 0, n-1)
    print (ans[0])
