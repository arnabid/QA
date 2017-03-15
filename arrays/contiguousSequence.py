# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:35:47 2016

@author: arnab
"""

""" Codility - caterpillar method, find a contiguous subsequence in an array
whose sum equals to a given number.
The elements are non-negative.
"""


def solutionV1(arr, k):
    """ *** ignore ***
    """
    n = len (arr)
    front, back, total = 0,0,0
    
    while (front < n and back < n):
        if total + arr[front] < k:
            total += arr[front]
            front += 1
        else:
            if total + arr[front] == k:
                print (back, front)
                total += arr[front]
                front += 1
            total -= arr[back]
            back += 1


def solution(arr,k):
    n = len(arr)
    
    # list of tuples; each tuple indicates the start and end of the contiguous
    # subsequence whose elements sum to k
    subSequences = []
    
    front, total = 0,0
    longestSeq = 0
    for back in xrange(n):
        # this inner loop breaks if front == n or total + arr[front] > k
        while front < n and total + arr[front] <= k:
            total += arr[front]
            front += 1
        if total == k:
            subSequences.append((back,front-1))
            longestSeq = max(longestSeq, front-back)
        
        if total < k and front == n:
            break
        total -= arr[back]
    
    return subSequences, longestSeq
            

if __name__ == '__main__':
    #arr = [3,2,7,3,1,1,2,1,12]
    arr = map(int, raw_input().strip().split(" "))
    k = int(raw_input())
    ans, longestSeq = solution(arr, k)
    print ("The contiguous subsequences whose sum of elements equals {0} are: {1}".format(k, ans))
    print ("The size of the longest subsequence is {0}".format(longestSeq))

