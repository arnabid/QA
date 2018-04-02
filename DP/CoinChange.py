# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:26:18 2016

@author: arnab
"""

""" Given certain coin denominations of unlimited quantities, find the minimum 
number of coins to get a value k """

from collections import Counter

def solution(coins, k):
    # A -> map with key = monetary value and the value = min # coins to get to key
    A, parent = Counter(coins), Counter()
    smallest_coin = min(coins)
    
    # no solution exists if k < smallest coin available
    if k < smallest_coin:
        return -1
    
    for c in coins:
        parent[c] = c
    
    for val in xrange(smallest_coin + 1, k + 1):
        if val not in A:
            mnwaysToval = float('inf')
            for c in coins:
                if val - c in A and A[val-c] + 1 < mnwaysToval:
                    mnwaysToval = A[val-c] + 1
                    A[val] = mnwaysToval
                    parent[val] = val-c

    # find the coins used to get k
    val = k
    if val in A:
        coins_used = []
        while parent[val] != val:
            coins_used.append(val - parent[val])
            val = parent[val]
        coins_used.append(val)
        print (coins_used)
    
    # return the min number of coins to make k; else return -1
    return A.get(k, -1)

if __name__ == '__main__':
    coins = [2,3,7]
    k = 11
    print (solution(coins,k))