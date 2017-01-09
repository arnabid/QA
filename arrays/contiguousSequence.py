# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:35:47 2016

@author: arnab
"""

""" Codility - caterpillar method, find a contiguous subsequence in an array
whose sum equals to a given number.
The elements must be non-negative.
"""

def solution(arr,k):
    n = len(arr)
    
    # list of tuples; each tuple indicates the start and end of the contiguous
    # subsequence whose elements sum to k
    ans = []
    
    front, total = 0,0
    longestSeq = 0
    for back in xrange(n):
        while front < n and total + arr[front] <= k:
            total += arr[front]
            front += 1
        if total == k:
            ans.append((back,front-1))
            longestSeq = max(longestSeq, front-back)
        total -= arr[back]
    
    return ans, longestSeq
            

if __name__ == '__main__':
    #arr = [3,2,7,3,1,1,2,1,12]
    arr = map(int, raw_input().strip().split(" "))
    k = int(raw_input())
    ans, longestSeq = solution(arr, k)
    print ("The contiguous subsequences whose sum of elements equals {0} are: {1}".format(k, ans))
    print ("The size of the longest subsequence is {0}".format(longestSeq))
