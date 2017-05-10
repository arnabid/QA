# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:40:28 2017

@author: arnab
"""

from collections import Counter

"""
time = O(n)
space = O(k); k = # distinct elements in array; worst case k = n
"""
def findMode(arr):
    c, maxfreq = Counter(), 0
    for x in arr:
        c[x] += 1
        if c[x] > maxfreq:
            maxfreq = c[x]
    
    for key in c:
        if c[key] == maxfreq:
            print (key),

def findMode2(arr):
    n = len(arr)
    arr.sort()
    
    # find the maxfreq
    count, maxfreq = 0, 0
    for i in xrange(n):
        count += 1
        if i < n-1 and arr[i] != arr[i+1]:
            maxfreq = max(maxfreq, count)
            count = 0
    maxfreq = max(maxfreq, count)
    
    # print all the elements in arr that have freq count = maxfreq
    count = 0
    for i in xrange(n):
        count += 1
        if i < n-1 and arr[i] != arr[i+1]:
            if count == maxfreq:
                print (arr[i]),
            count = 0
    
    if count == maxfreq:
        print arr[-1]

if __name__ == '__main__':
    arr = [1,2,2,3,3,3,4,4,4,4]
    findMode(arr)
    print("")
    findMode2(arr)