# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:49:50 2016

@author: arnab
"""

""" Remove elements from the end of an array such that 2*min > max
find the minimum number of elements that have to be removed. 
Bonus: Find all possible combinations """


def solution(ml):
    n = len(ml)
    longest_start,longest_end = 0,0
    
    # list of tuples (start,end); each tuple indicates the starting and ending index of
    # subsequence left after removing minimum number of elements.
    ans = []
    
    for start in xrange(n):
        min,max = float('inf'),-float('inf')
        
        for end in xrange(start,n):
            val = ml[end]
            
            if val < min:
                min = val
            if val > max:
                max = val
            
            if 2*min <= max:
                break
            
            if end - start > longest_end - longest_start:
                ans = [(start,end)]
                longest_start = start
                longest_end = end
                continue
            if end - start == longest_end - longest_start:
                ans.append((start,end))
            
    
    print (ans)
    print (n - (longest_end - longest_start + 1))

if __name__ == '__main__':
    ml = [1,2,3,4,5,6,7,8,9,10]
    #ml = [4,5,100,9,10,11,12,15,200]
    #ml = [20,4,1,3]
    solution(ml)
