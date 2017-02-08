# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 10:49:25 2016

@author: arnab
"""

""" Codility - Break the Chain
Key observation: One of the combination of 4 smallest numbers is the desired answer
because all 4 of them cannot be adjacent to each other.
"""

""" Time complexity : N^2 """
def solution2(ml):
    res = float('inf')
    n = len(ml)
    for back in xrange(1,n-3):
        front = back + 2
        while front < n-1:
            res = min(res, ml[back]+ml[front])
            #print (ml[back],ml[front])
            front += 1
    return res

""" Time complexity : N """
def solution(ml):
    
    maxe = float('inf')
    n = len(ml)
    
    """ The part of the array where the links can be broken, excluding the 2 boundary elements """
    part = ml[1:n-1]
    
    """ min1 <= min2 <= min3 <= min4 """
    """ Find the 2 smallest elements """
    min1, min1index = float('inf'), -1
    min2, min2index = float('inf'), -1
    for i in xrange(len(part)):
        if part[i] < min1:
            min2 = min1
            min2index = min1index
            min1 = part[i]
            min1index = i
        elif part[i] < min2:
            min2 = part[i]
            min2index = i
    
    #print (min1,min2,min1index,min2index)
    if abs(min1index - min2index) != 1:
        return min1 + min2
    
    part[min1index] = maxe
    part[min2index] = maxe
    
    """ Find the 3rd and 4th smallest elements """
    min3, min3index = float('inf'), -1
    min4, min4index = float('inf'), -1
    for i in xrange(len(part)):
        if part[i] < min3:
            min4 = min3
            min4index = min3index
            min3 = part[i]
            min3index = i
        elif part[i] < min4:
            min4 = part[i]
            min4index = i
    
    #print (min3,min4,min3index,min4index)
    if abs(min1index - min3index) != 1:
        return min1 + min3
    elif min1 + min4 <= min2 + min3:
        if abs(min1index - min4index) != 1:
            return min1 + min4
    elif min1 + min4 > min2 + min3:
        if abs(min2index - min3index) != 1:
            return min2 + min3
#    elif abs(min2index - min4index) != 1:
#        return min2 + min4
    else:
        return min2 + min4


if __name__ == '__main__':
    ml = [9,10,8,2,5,7,1,10]
    answer = solution(ml)
    print ("The minimum cost to break the chain in 3 pieces is %d" %answer)
