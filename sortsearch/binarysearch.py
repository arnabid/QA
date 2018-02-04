# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 09:20:57 2017

@author: arnab
"""

# recursive binary search
def binarysearch(arr, low, high, key):
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


# iterative binary search
def iterativeBS(arr,low,high,key):
    
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid+1
        else:
            high = mid-1
    return -1


# used in bisect_left and bisect_right routines
def iterativeBSCustom(arr,low,high,key):
    
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == key:
            return mid, 1
        elif arr[mid] < key:
            low = mid+1
        else:
            high = mid-1
    return low, 0


# number of elements in arr <= key
def bisect_right(arr, low, high, key):
    right, found = iterativeBSCustom(arr, low, high, key)
    if not found:
        return right
    while right < high and arr[right+1] == key:
        right, found = iterativeBSCustom(arr, right+1, high, key)
    return right+1


# number of elements in arr >= key
def bisect_left(arr, low, high, key):
    left, found = iterativeBSCustom(arr, low, high, key)
    if not found:
        return high-left+1
    while left > 0 and arr[left-1] == key:
        left = iterativeBS(arr, low, left-1, key)
    return high-left+1


# number of elements in arr == key
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
    mylist = [1,1,2,3,5,5,5,5,7,8,10]
    low, high = 0, len(mylist)-1

    # bisect_right
    print (bisect_right(mylist,low, high, 0)) #0
    print (bisect_right(mylist,low, high, 1)) #2
    print (bisect_right(mylist,low, high, 2)) #3
    print (bisect_right(mylist,low, high, 3)) #4
    print (bisect_right(mylist,low, high, 5)) #8
    print (bisect_right(mylist,low, high, 9)) #10
    print (bisect_right(mylist,low, high, 10)) #11
    print (bisect_right(mylist,low, high, 15)) #11

    # bisect_left
    print (bisect_left(mylist,low, high, 0)) #11
    print (bisect_left(mylist,low, high, 1)) #11
    print (bisect_left(mylist,low, high, 2)) #9
    print (bisect_left(mylist,low, high, 4)) #7
    print (bisect_left(mylist,low, high, 5)) #7
    print (bisect_left(mylist,low, high, 9)) #1
    print (bisect_left(mylist,low, high, 10)) #1
    print (bisect_left(mylist,low, high, 15)) #0

    # number of occurences
    print (numberOfOccurences(mylist, low, high, 5)) #4
    print (numberOfOccurences(mylist, low, high, 7)) #1
    print (numberOfOccurences(mylist, low, high, 21)) #0

