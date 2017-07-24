# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 07:51:53 2017

@author: arnab
"""

"""
Boyer-Moore algorithm for finding the majority element
majority element - count >= (n//2) + 1
O(N) time; O(1) space
reference: https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
"""

def findMajorityElement(arr):
    # returns majority element if it exists; else returns None
    count, candidate = 0, 0
    n = len(arr)
    
    # find the candidate value
    for x in arr:
        if count == 0:
            candidate = x
        if x == candidate:
            count += 1
        else:
            count -= 1
    
    # verify candidate
    if count >= (n//2)+1:
        print "Hello"
        return candidate

    count = 0
    for x in arr:
        if x == candidate:
            count += 1
    if count >= (n//2)+1:
        return candidate
    return None

if __name__ == '__main__':
    arr = [0,0,1,1,1]
    print (findMajorityElement(arr))
        
    