# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:19:14 2016

@author: arnab
"""

""" Random shuffling of elements in an array[]
Why does this work?

We have to prove that the probability(pr) that an ith element goes to any position 
in the array is equal. (for all elements and all positions).
Or another way to think about it is that any position in the array has equal pr of holding
any of the elements in the array.

Pr that the ith element including the 1st element goes to the 1st postion = 1/N

Pr that the ith element goes to the 2nd position:

Case 1: consider the 1st element
pr that the 1st element goes to the 2nd position = pr that the same index x gets picked twice,
first in [0..N-1] and then in [1...N-1]; note that x can take any values except the 1st index
pr = N-1/N * 1/N-1 = 1/N

Case 2: consider all the other elements
pr that the ith element goes to the 2nd position = pr that the ith element does not get picked
in the first iteration * pr that the ith element gets picked in the 2nd iteration
pr = N-1/N * 1/N-1 = 1/N

We just proved that 1st and 2nd position can hold any element with equal probability = 1/N
We can generalize the above proof for any other position.
"""

import random

def shuffle(ml):
    n = len(ml)
    for i in xrange(n):
        # exchange a[i] with a random element in a[i...N-1]
        r = random.randint(i,n-1)
        ml[i], ml[r] = ml[r], ml[i]

if __name__ == '__main__':
    ml = [1,2,3,4,5,6,7,8]
    
    # before shuffle
    print (ml)
    
    # do the shuffle
    shuffle(ml)
    
    # after shuffle
    print (ml)