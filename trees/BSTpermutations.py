# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 08:23:27 2017

@author: arnab
"""
from collections import Counter
from math import factorial

class BST(object):
    def __init__(self, *values):
        self.root = None
        self.left = None
        self.right = None
        self.count = 0
        self.ip = 1
        
        for value in values:
            self.insert(value)
    
    def insert(self, value):
        if self.root is None:
            self.root = value
        elif value < self.root:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)

def getchildren(node):
    children = []
    if node.left:
        children.append(node.left)
    
    if node.right:
        children.append(node.right)
    return children
    
def choose(n, k):
    """
    Calculates the binomial coefficient for n, k.
    This is equivalent to 'n choose k'.
    """
    return factorial(n) / (factorial(k) * factorial(n - k))
    

def solution(root):
    visited = Counter()
    
    def dfs(v):
        visited[v] = True
        for w in getchildren(v):
            if not visited.get(w, False):
                dfs(w)
        #backtrack
        ls, rs = 0, 0
        lp, rp = 1, 1
        if v.left:
            ls = v.left.count
            lp = v.left.ip
        if v.right:
            rs = v.right.count
            rp = v.right.ip
        v.count = ls + rs + 1
        v.ip = choose(ls + rs, rs) * lp * rp

    dfs(root)
        

if __name__ == '__main__':
    seq = [5, 9, 8, 2, 1]
    root = BST(*seq)
    
    solution(root)
    ls, rs = 0, 0
    lp, rp = 1, 1
    if root.left:
        ls = root.left.count
        lp = root.left.ip
    if root.right:
        rs = root.right.count
        rp = root.right.ip
    ans = choose(ls + rs, rs) * lp * rp
    print(ans)
    
    # what do i need at each node: ls, rs, lp, rp