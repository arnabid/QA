# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 07:52:15 2016

@author: arnab
"""
"""
given n - size of n*n matrix, r, c
find the number at A[r][c].
The matrix is filled in an anti-clockwise spiral fashion
beginning at the center of the matrix.
"""

if __name__ == '__main__':
    n,r,c = map(int, raw_input().strip().split(" "))
    assert (r >= 0 and r < n), "Inavlid row index"
    assert (c >= 0 and c < n), "Invalid column index"
    i,j = 0,0
    if n%2:
        i,j = (n-1)//2, (n-1)//2
    else:
        i,j = n//2 - 1, n//2
    
    #print (i,j)
    count = 1
    col = True
    number = 1
    sign = 1
    while (i,j) != (r,c) and count <= (n*n):
        if col:
            if number%2:
                sign = -1
            else:
                sign = 1
            for k in xrange(1,number+1):
                j += sign
                count += 1
                #print (i,j)
                if (i,j) == (r,c):
                    break
            col = not col
        else:
            if number%2:
                sign = 1
            else:
                sign = -1
            for k in xrange(1,number+1):
                i += sign
                count += 1
                #print (i,j)
                if (i,j) == (r,c):
                    break
            col = not col
            number += 1
    print (count)
