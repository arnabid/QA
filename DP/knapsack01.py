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
recursion with memoization
"""
def knapsack(W, wt, val, n, table):
    if W == 0 or n == 0:
        return 0
    
    if (W, n) in table:
        return table[(W,n)][0]
    
    if wt[n-1] > W:
        return knapsack(W, wt, val, n-1, table)
    
    c1 = val[n-1] + knapsack(W-wt[n-1], wt, val, n-1, table)
    c2 = knapsack(W, wt, val, n-1, table)
    
    # item n was selected; 0 - left; 1 - right
    if c1 > c2:
        table[(W,n)] = (c1,0)
    else:
        table[(W,n)] = (c2,1)
    return table[(W,n)][0]

if __name__ == '__main__':
    W = 80
    wt = [40,20,30]
    val = [160,100,120]
    table = Counter()
    n = len(val)
    print (knapsack(W, wt, val, n, table))
    print (table)
    
    node = (W,n)
    select = []
    while node in table:
        if table[node][1] == 0:
            select.append(node[1])
            node = (node[0]-wt[node[1]-1], node[1]-1)
        else:
            node = (node[0], node[1]-1)
    print (select)


    