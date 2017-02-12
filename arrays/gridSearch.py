# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:56:52 2017

@author: arnab
"""

"""
find a pattern in a grid
reference: https://www.hackerrank.com/challenges/the-grid-search
"""

if __name__ == '__main__':
    # iterate over every element in grid  
    for _ in xrange(input()):
        big = []
        small = []
        R, C = map(int, raw_input().strip().split(" "))
        for __ in range(R):
            big.append(raw_input().strip())
        r, c = map(int, raw_input().strip().split(" "))
        for __ in range(r):
            small.append(raw_input().strip())
        found = False
        for i in range(R - r + 1):
            for j in range(C - c + 1):
                flag = True
                for k in range(r):
                    for l in range(c):
                        if big[i + k][j + l] != small[k][l]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print ("YES")
                    found = True
                    break
            if found:
                break
        if not found:
            print ("NO")