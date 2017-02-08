# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:26:18 2016

@author: arnab
"""

""" Given certain coin denominations of unlimited quantities, find the minimum 
number of coins to get a value k """

def solution(coins, k):
    # A -> map with key = M and the value = min coins to get M
    A, parent = {}, {}
    
    minc = min(coins)
    
    if k < minc:
        return -1
    
    for c in coins:
        A[c] = 1
        parent[c] = c
    
    for i in xrange(minc+1, k+1):
        if i not in A:
            A[i] = float('inf')
            for c in coins:
                if A.get(i-c, float('inf')) + 1 < A[i]:
                    parent[i] = i-c
                    A[i] = A.get(i-c, float('inf')) + 1
    
    print A, "\n"
    print parent, "\n"
    
    number_of_coins = A[k]

    # find the coins used to get k
    coins_used = []
    
    while parent[k] != k:
        coins_used.append(k - parent[k])
        k = parent[k]
    coins_used.append(k)
    print (coins_used)

    return number_of_coins

if __name__ == '__main__':
    coins = [9,6,5,1]
    k = 19
    print (solution(coins,k))