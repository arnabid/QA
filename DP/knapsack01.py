# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:53:46 2017

@author: arnab
"""
from collections import Counter

"""
W - weight capacity of knapsack
wt - weight array, val - value array
n - # items
"""

"""
DP, O(n*W)
"""
def ksDP(W, wt, val, n):
    table = [[0] * (W+1)] * (n+1)
    
    for i in xrange(1,n+1):
        for w in xrange(1,W+1):
            if wt[i] <= w:
                if val[i] + table[i-1][w-wt[i]] > table[i-1][w]:
                    table[i][w] = val[i] + table[i-1][w-wt[i]]
                else:
                    table[i][w] = table[i-1][w]
            else:
                table[i][w] = table[i-1][w]
    
    # find the optimal knapsack
    i, w = n, W
    knapsack = []
    while i > 0 and w > 0:
        if table[i][w] != table[i-1][w]:
            knapsack.append(i)
            i = i - 1
            w = w - wt[i]
        else:
            i = i - 1
            
    return table[n][W], knapsack


"""
recursive solution with memoization
"""
def ksRecursion(W, wt, val, n, table):
    if W == 0 or n == 0:
        return 0
    
    if (W, n) in table:
        return table[(W,n)][0]
    
    if wt[n-1] > W:
        return ksRecursion(W, wt, val, n-1, table)
    
    c1 = val[n-1] + ksRecursion(W-wt[n-1], wt, val, n-1, table)
    c2 = ksRecursion(W, wt, val, n-1, table)
    
    # item n was selected; 0 - left; 1 - right
    if c1 > c2:
        table[(W,n)] = (c1,0)
    else:
        table[(W,n)] = (c2,1)
    
    # find the optimal knapsack
    node = (W,n)
    knapsack = []
    while node in table:
        if table[node][1] == 0:
            knapsack.append(node[1])
            node = (node[0]-wt[node[1]-1], node[1]-1)
        else:
            node = (node[0], node[1]-1)
    print (knapsack)
    return table[(W,n)][0], knapsack

if __name__ == '__main__':
    W = 80
    wt = [40,20,30]
    val = [160,100,120]
    table = Counter()
    n = len(val)
    print (ksRecursion(W, wt, val, n, table))


    