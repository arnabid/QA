# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 20:00:52 2016

@author: arnab
"""

if __name__ == '__main__':
    n = 6
    for l in xrange(2,n+1):
        for i in xrange(1,n-l+2):
            j = i + l - 1
            print ((i,j))
