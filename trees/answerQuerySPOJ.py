# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 21:43:38 2017

@author: arnab
"""

def maxSubArraySum(a,low, high):
     
    max_so_far =a[low]
    curr_max = a[low]
     
    for i in range(low+1,high+1):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far

if __name__ == '__main__':
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(" "))
    
    #total = [0]*n
    m = int(raw_input().strip())

    for _ in xrange(m):
        x, y = map(int, raw_input().strip().split(" "))
        x -= 1
        y -= 1
        print (maxSubArraySum(arr,x,y))
#        ans = -float('inf')
#        for i in xrange(x,y+1):
#            for j in xrange(i,y+1):
#                if i == j:
#                    total[j] = arr[j]
#                else:
#                    total[j] = total[j-1] + arr[j]
#                ans = max(ans, total[j])
#        print (ans)