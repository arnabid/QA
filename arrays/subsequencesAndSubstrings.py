# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 22:43:33 2017

@author: arnab
"""

"""
all about contiguous subsequences and substrings
Find if cintiguous subsequence of array sums to target
"""

"""
version 1 - O(N^2)
Handles negative numbers
"""
def version1(arr, target):
    n = len(arr)
    # pick a starting point
    for i in xrange(n):
        temp = 0
        for j in xrange(i,n):
            temp += arr[j]
            if temp == target:
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
    totalSum, n = arr[0], len(arr)
    prefixSum = [0]*n
    suffixSum = [0]*n
    
    # calculate prefixSum, suffixSum, totalSum
    for i in xrange(1,n):
        prefixSum[i] = prefixSum[i-1]+arr[i-1]
        suffixSum[n-i-1] = suffixSum[n-i] + arr[n-i]
        totalSum += arr[i]
    
    for i in xrange(n):
        for j in xrange(i,n):
            if totalSum-prefixSum[i]-suffixSum[j] == target:
                return (i,j)

"""
version3 - using a map
O(N) time; O(N) - space
Handles negative numbers
"""
def version3(arr, target):
    n = len(arr)
    prefixsum = {}
    currentSum = 0
    for i in xrange(n):
        currentSum += arr[i]
        if currentSum == target:
            return (0, i)
        # this implies that there exists a subarray thats sums to target
        if (currentSum-target) in prefixsum:
            return (prefixsum[currentSum-target]+1, i)
        prefixsum[currentSum] = i


"""
another variance of this question:
find the number of subarrays that sum to target
reference: https://leetcode.com/problems/subarray-sum-equals-k/description/
"""
def subarraySumCount(arr, target):
    n = len(arr)
    prefixsum = {}
    currentSum, ans = 0, 0
    for i in xrange(n):
        currentSum += arr[i]
        if currentSum == target:
            ans += 1
        if (currentSum-target) in prefixsum:
            ans += len(prefixsum[currentSum-target])
        if currentSum in prefixsum:
            prefixsum[currentSum].append(i)
        else:
            prefixsum[currentSum] = [i]
    return ans


"""
version 3 - caterpillar method
time - O(N)
*** Does not handle negative numbers
"""
def version4(arr, target):
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
    #print (version1(arr, 7))
    #print (version2(arr, 4))
    print (version3(arr, 3))
    #print (version4(arr, 7))