# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:01:53 2016

@author: arnab
"""

""" 3-SUM in quadratic time. Find all triplets that add to a given sum in 
array of N distinct integers.
"""            

def threeSum(arr,sp):
    n = len(arr)
    arr.sort()
    count = 0
    triplets = []
    
    for i in xrange(n-2):
        if arr[i] < sp:
            j,k = i+1, n-1
            while(j<k):
                if arr[j] + arr[k] + arr[i] == sp:
                    count += 1
                    triplets.append([arr[i],arr[j],arr[k]])
                    j += 1
                    k -= 1
                elif arr[j] + arr[k] + arr[i] < sp:
                    j += 1
                else:           #arr[j] + arr[k] + arr[i] > sp
                    k -= 1
        else:
            break

    print (triplets)
    return count

if __name__ == '__main__':
    arr = [7,6,2,11,5]
    sp = 18
    count = threeSum(arr,sp)
    print ("The number of triplets that sum to %d is %d" %(sp,count))
