# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 12:01:09 2016

@author: arnab
"""
"""
https://www.hackerrank.com/challenges/swap-nodes-algo
"""
import sys
from collections import Counter
import Queue
sys.setrecursionlimit(1500)

class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)

if __name__ == '__main__':
    n = int(raw_input())
    nodes = [0]
    for _ in xrange(1, n+1):
        nodes.append(map(int, raw_input().strip().split(" ")))
    root = Node(1)
    q = Queue.Queue()
    q.put((root, 1))
    maxheight = 1
    
    levels = Counter()
    levels[1] = [root]
    while not q.empty():
        v, ch = q.get()
        lval, rval = nodes[v.val]
        if lval != -1:
            lc = Node(lval)
            v.left = lc
            q.put((lc, ch+1))
            maxheight = ch+1
            if ch+1 in levels:
                levels[ch+1].append(lc)
            else:
                levels[ch+1] = [lc]
        if rval != -1:
            rc = Node(rval)
            v.right = rc
            q.put((rc, ch+1))
            maxheight = ch+1
            if ch+1 in levels:
                levels[ch+1].append(rc)
            else:
                levels[ch+1] = [rc]

    T = int(raw_input())
    for _ in xrange(T):
        k = int(raw_input())
        t = k
        while t < maxheight:
            for node in levels[t]:
                node.left, node.right = node.right, node.left
            t += k
        printInorder(root)
        print ("")
