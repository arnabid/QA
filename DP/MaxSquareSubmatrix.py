# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 15:20:10 2016

@author: arnab
"""

""" TODO: maximum size rectangular sub-matrix"""

def solutionRectangle(ml):
    pass

""" Given a matrix of dimensions mxn having all entries as 1 or 0,
find out the size of maximum size square sub-matrix with all 1s. 
Also return the area of the square sub-matrix """

def solutionSquare(ml):
    m,n = len(ml), len(ml[0])
    
    a = [[0 for i in xrange(n)] for i in xrange(m)]
    a.remove()
    maxn = 0
    
    # make the first row the same
    for i in xrange(n):
        a[0][i] = ml[0][i]
        maxn = max(maxn, a[0][i])

    # make the first column the same
    for j in xrange(m):
        a[j][0] = ml[j][0]
        maxn = max(maxn, a[j][0])
    
    for i in xrange(1,m):
        for j in xrange(1,n):
            if ml[i][j] == 0:
                a[i][j] = 0
            else:
                a[i][j] = min(a[i-1][j-1], a[i][j-1], a[i-1][j]) + 1
                maxn = max(maxn, a[i][j])
    
    return maxn, maxn ** 2

if __name__ == '__main__':
    ml = [[0,1],[1,0]]
    print (solutionSquare(ml))