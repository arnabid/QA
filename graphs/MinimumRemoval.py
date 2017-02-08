# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 09:52:54 2016

@author: arnab
"""

""" Remove minimum elements from an array so that 2 * min > max
"""
import heapq

def solution(ml):
    n = len(ml)
    count,i,j = 0,0,n-1
    
    tempmin = []
    tempmax = []
    
    # build the 2 heaps
    for item in ml:
        heapq.heappush(tempmin,item)
        heapq.heappush(tempmax,(-item))
    
    while i <= j:
        if 2*tempmin[0] > -tempmax[0]:
            return count
        
        x,y = 0,0
        tempmin = []
        tempmax = []
        # delete ml[i] from both heaps
        tempmin = ml[i+1:j+1]
        heapq.heapify(tempmin)
        
        tempmax = [-item for item in ml[i+1:j+1]]
        heapq.heapify(tempmax)
        
        x = -tempmax[0] - 2*tempmin[0]
        
        # delete ml[j] from both heaps
        tempmin = ml[i:j]
        heapq.heapify(tempmin)
        
        tempmax = [-item for item in ml[i:j]]
        heapq.heapify(tempmax)
        
        y = -tempmax[0] - 2*tempmin[0]
        
        if x < y: # delete ml[i]
            # construct both heaps with ml[j] in it
            tempmin = ml[i+1:j+1]
            heapq.heapify(tempmin)
            tempmax = [-item for item in ml[i+1:j+1]]
            heapq.heapify(tempmax)
            i += 1
            count += 1
        else: # delete ml[j]
            tempmin = ml[i:j]
            heapq.heapify(tempmin)
            tempmax = [-item for item in ml[i:j]]
            heapq.heapify(tempmax)
            j -= 1
            count += 1
    return count


if __name__ == '__main__':
    ml = [4,5,100,9,10,11,12,15,200]
    #ml = [1,2,3,4,5,6,7,8,9,10]
    #ml = [1,2,3,4,5,6,1,2,3,10]
    count = solution(ml)
    print (count)
