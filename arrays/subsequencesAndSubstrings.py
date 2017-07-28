# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 22:43:33 2017

@author: arnab
"""

"""
all about contiguous subsequences and substrings
"""

"""
most naive approach - O(N^3)
Handles negative numbers
"""
def version1(arr, target):
    n = len(arr)
    for i in xrange(n):
        for j in xrange(i,n):
            t = 0
            for k in xrange(i,j+1):
                t += arr[k]
            if t == target:
                return (i,j)


"""
version 2 - using prefix and suffix sums
sum of arr[p]; p = [i...j] = totalSum - prefixSum[i] - suffixSum[j]
prefixSum[i] = sum of arr[p]; p = [0...i)
suffixSum[i] = sum of arr[p]; p [i+1...n)

time - O(N^2); space - O(N)
Handles negative numbers
"""

def version2(arr, target):
    totalSum, n = sum(arr), len(arr)
    prefixSum = [0]*n
    suffixSum = [0]*n
    
    # populate prefixSum
    for i in xrange(1,n):
        prefixSum[i] = prefixSum[i-1]+arr[i-1]

    # populate suffixSum
    for i in xrange(n-2,-1,-1):
        suffixSum[i] = suffixSum[i+1]+arr[i+1]
    
    for i in xrange(n):
        for j in xrange(i,n):
            if totalSum-prefixSum[i]-suffixSum[j] == target:
                return (i,j)

"""
version 3 - caterpillar method
time - O(N)
*** Does not handle negative numbers
"""
def version3(arr, target):
    n = len(arr)
    back = front = total = 0
    while back < n:
        # this inner loop breaks if front == n or total + arr[front] > k
        while front < n and total + arr[front] <= target:
            total += arr[front]
            if total == target:
                return (back, front)
            front += 1
        total -= arr[back]
        back += 1


if __name__ == '__main__':
    arr = [1,2,3,4]
    #print (version1(arr, 0))
    #print (version2(arr, 0))
    print (version3(arr, 5))