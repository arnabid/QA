# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:06:27 2016

@author: arnab
"""

""" Reservoir sampling:
TODO: Add link to geeksforgeeks article


Notes:
The problem is to randomly choose k items from a list of n items.
Applications:
Challenges:

stream[] - input stream, size = n
reservoir[] - output list of randomly chosen k items, size = k

solution: Copy the first k items from stream[] to reservoir[]
Then for each index i from k+1 to n, generate a random number j in the range (1,i)
If j is in the range (1,k), then replace reservoir[j] with stream[i]

Why does this work? To prove it works, we must prove that the probability that any item
in the stream[] ends up in the final reservoir[] is equal.

First case: Consider the first k items that are initially copied to reservoir[]
The probability that any one of these items in say index x (1<=x<=k) remains in the final reservoir[]
is that x is not picked in iterations k+1 to n
P = (k/k+1)*(k+1/k+2)*..*(n-1/n) = k/n

k/k+1 --> pick the remaining k places except x in k+1 places and so on...

Second case: what is the probability that any item from k+1 to n ends up in the final reservoir[]?
consider the last item: the prob that it is placed in the reservoir[] = k/n
2nd last item: the only way it will be in the final reservoir[] is that one of the k places
gets chosen in the n-1 iteration and the that same place does not get chosen again in the nth iteration
P = k/n-1 * n-1/n = k/n
"""
import random

def selectkitems(stream, k):
    # returns k randomly chosen elements from the input stream[]

    n = len(stream)
    if k > n:
        raise Exception("Number of items to select is greater than array size.")

    reservoir = stream[0:k]
    for i in xrange(k,n):
        j = random.randint(0,i)
        if j >= 0 and j < k:
            reservoir[j], stream[i] = stream[i], reservoir[j]
    
    return reservoir


if __name__ == '__main__':
    stream = [i for i in xrange(1,51)]
    reservoir = selectkitems(stream, 100)
    
    print (reservoir)
