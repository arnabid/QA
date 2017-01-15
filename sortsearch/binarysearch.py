# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 09:20:57 2017

@author: arnab
"""

def binarysearch(arr,low,high,key):
    # returns the index of key or -1 if key not found
    
    if low > high:
        return -1
    
    mid = low + (high-low)/2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binarysearch(arr,mid+1,high,key)
    else:
        return binarysearch(arr,low,mid-1,key)

def iterativeBS(arr,low,high,key):
    
    while low <= high:
        mid = low + (high-low)/2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid+1
        else:
            high = mid-1
    print (low) # index where the new key should be inserted
    return -1

def numberOfOccurences(arr, low, high, key):
    # returns the number of occurences of key in arr
    index = iterativeBS(arr, low, high, key)
    if index == -1:
        return 0
    left, right = index, index
    # find the leftmost index i such that arr[i] = key
    while left > 0 and arr[left-1] == key:
        left = iterativeBS(arr, low, left-1, key)
    # find the rightmost index i such that arr[i] = key
    while right < high and arr[right+1] == key:
        right = iterativeBS(arr, right+1, high, key)
    return right-left+1


if __name__ == '__main__':
    mylist = [1,1,1,1,5,5,5,5,5]
    low, high = 0, len(mylist)-1
    # print (iterativeBS(mylist,low,high,1)
    print (numberOfOccurences(mylist, low, high, 5))
