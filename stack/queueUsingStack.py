# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 07:54:03 2016

@author: arnab
"""

"""
implement a queue using a stack
operations supported:
add: add an item to the queue
get: remove and return the item at the front of the queue
head: return the item at the front of the queue
tail: return the item at the end of the queue

Input format:
1 x -> add x to the queue
2 -1-> get the item from the queue
3 -1-> return the head of the queue
4 -1-> return the tail of the queue
*** requires more testing ***
"""

if __name__ == '__main__':
    T = int(raw_input())
    eq, dq = [], []
    for _ in xrange(T):
        x, y = map(int, raw_input().strip().split(" "))
        if x == 1:
            eq.append(y)
        elif x == 2:
            if dq:
                print (dq.pop())
            else:
                while eq:
                    dq.append(eq.pop())
                print (dq.pop())
        elif x == 3:
            if dq:
                print (dq[-1])
            else:
                print (eq[0])
        else:
            if eq:
                print (eq[-1])
            else:
                print (dq[0])
