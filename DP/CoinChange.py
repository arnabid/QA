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
                if val - c in A and A[val-c] < mnwaysToval:
                    mnwaysToval = A[val-c] + 1
                    parent[val] = val-c
            if mnwaysToval < float('inf'):
                A[val] = mnwaysToval

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
    coins = [5,7,8]
    k = 18
    print (solution(coins,k))