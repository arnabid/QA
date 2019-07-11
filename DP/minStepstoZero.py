# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 07:54:24 2017

@author: arnab
"""
"""
problem statement: https://www.hackerrank.com/challenges/down-to-zero-ii
"""

from collections import Counter

if __name__ == '__main__':
    table = Counter({0:0, 1:1})
    # fill the table for the entire input range ~ O(n*n)
    for i in range(2,21):
        table[i] = min(table.get(i, float('inf')), 1 + table[i-1])
        # fill all the slots for the product of i*{2...i}
        for x in range(2, min(21//i, i)+1):
            table[i*x] = min(table.get(i*x, float('inf')), 1 + table[i])
    print (table)

    """
    q = int(raw_input())
    for _ in xrange(q):
        n = int(raw_input())
        print (table[n])
    """