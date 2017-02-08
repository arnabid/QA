# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:01:53 2016

@author: arnab
"""

""" Find all the triplets that can form a triangle
(i.e) (x,y,z) such that: a[x] + a[y] > a[z]
"""

import random


""" Geeksforgeeks """
def findnumberofTriangles(arr):
    n = len(arr)
    arr.sort()
    count = 0
    
    for i in range(0,n-2):
        k = i + 2
        for j in range(i+1,n):
            while (k < n and arr[i] + arr[j] > arr[k]):
                k += 1
            count += k - j - 1
    return count


""" My solution """
def numTriangles(ml):
    ml.sort()
    print (ml)
    
    n = len(ml)
    count = 0
    
    for largest in xrange(n-1,1,-1):
        front,back = 0,largest-1
        while front < back:
            if ml[front] + ml[back] > ml[largest]:
                count += back - front
                back -= 1
                continue
            else:
                front += 1
    return count


if __name__ == '__main__':
    ml = [3,3,3,3]
    #ml = [random.randint(1,20) for x in range(10)]
    count1 = numTriangles(ml)
    count2 = findnumberofTriangles(ml)
    print ("The number of triangles is %d, %d" %(count1,count2))
