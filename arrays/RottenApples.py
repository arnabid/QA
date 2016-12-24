# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 09:32:36 2016

@author: arnab
"""


""" Inplace no extra space except for the Queue
    2 - rotten apple
    1 - good apple
    0 - empty space
    
    The apples adjacent(left,right,top,bottom) to the rotten apples get spoilt in 1 unit of time.
    Find the time it takes for all apples to get spoilt if possible. If not, also find the apples
    that do not get spoilt.
"""
import Queue
import random

def solution(A):
    r, c = len(A), len(A[0])
    q = Queue.Queue()
    # Put the 2s in the queue
    for i in range(r):
        for j in range(c):
            if A[i][j] == 2:
                q.put((i,j))
    
    tR = 2
    rn = [-1,0,1,0]
    cn = [0,1,0,-1]
    while not q.empty():
        (i,j) = q.get()
        ntime = A[i][j] + 1
        # check adjacent cells of (i,j)
        for k in xrange(4):
            ii = i + rn[k]
            jj = j + cn[k]
            if (ii >= 0 and ii < r) and (jj >= 0 and jj < c) \
            and A[ii][jj] == 1:
                A[ii][jj] = ntime
                tR = max(tR, ntime)
                q.put((ii,jj))
    
    for i in range(r):
        for j in range(c):
            if A[i][j] == 1:
                print ("The apple in position ({},{}) cannot get spoilt".format(i,j))
    
    print ("Apples which can get spoilt will do so in {} unit(s) of time.".format(tR-2))
    

if __name__ == '__main__':
    m, n = map(int, raw_input().strip().split(" "))
    grid = [[random.randint(0,2) for x in range(n)] for x in range(m)]
    print (grid)
    solution(grid)
    print (grid)