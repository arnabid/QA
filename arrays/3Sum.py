# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:01:53 2016

@author: H138576
"""

""" 3-SUM in quadratic time. Find all triplets that add to a given sum in 
array of N distinct integers.
"""            

def threeSum(ml,sp):
    n = len(ml)
    ml.sort()
    print (ml)
    count = 0
    triplets = []
    
    for i in xrange(n-2):
        if ml[i] < sp:
            j,k = i+1, n-1
            while(j<k):
                if ml[j] + ml[k] + ml[i] == sp:
                    count += 1
                    triplets.append([ml[i],ml[j],ml[k]])
                    j += 1
                    k -= 1
                    continue
                elif ml[j] + ml[k] + ml[i] < sp:
                    j += 1
                    continue
                else:           #ml[j] + ml[k] + ml[i] > sp
                    k -= 1
                    continue
        else:
            break

    print (triplets)
    return count

if __name__ == '__main__':
    ml = [7,6,2,11,5]
    sp = 18
    count = threeSum(ml,sp)
    print ("The number of triplets that sum to %d is %d" %(sp,count))
