# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 07:56:55 2017

@author: arnab

Summed Area Table
reference: http://www.geeksforgeeks.org/summed-area-table-submatrix-summation/
"""
import random

if __name__ == '__main__':
    m,n = map(int, raw_input().strip().split(" "))
    arr = [[random.randint(1,3) for x in xrange(n)] for x in xrange(m)]
    print (arr)
    
    # populate sumarr[]
    sumarr = [[0 for x in xrange(n)] for x in xrange(m)]
    sumarr[0][0] = arr[0][0]
    for j in xrange(1,n):
        sumarr[0][j] = sumarr[0][j-1] + arr[0][j]
    
    for i in xrange(1,m):
        sumarr[i][0] = sumarr[i-1][0] + arr[i][0]
    
    for i in xrange(1, m):
        for j in xrange(1, n):
            sumarr[i][j] = sumarr[i-1][j] + sumarr[i][j-1] + arr[i][j] - sumarr[i-1][j-1]
    
    print (sumarr)
    
    # input (tli, tlj) and (rbi, rbj)
    tli, tlj, rbi, rbj = map(int, raw_input().strip().split(" "))
    total = sumarr[rbi][rbj]
    
    if tli > 0:
        total -= sumarr[tli-1][rbj]
    
    if tlj > 0:
        total -= sumarr[rbi][tlj-1]
    
    if tli > 0 and tlj > 0:
        total += sumarr[tli-1][tlj-1]
    
    print (total)