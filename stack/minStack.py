# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 16:40:11 2017

@author: arnab
"""

"""
Design a data structure that supports the following operations:
push
pop
findMin

notes:
stack: contains elements
mstack[-1]: is the min element of elements present in stack

observation:
if stack is not empty it implies that mstack is also not empty.
"""

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.mstack = []
    
    def push(self, x):
        if self.mstack:
            if x <= self.mstack[-1]:
                self.mstack.append(x)
        self.stack.append(x)
    
    def pop(self):
        if self.stack:
            if self.stack[-1] == self.mstack[-1]:
                self.mstack.pop()
            return self.stack[-1]
    
    def findMin(self):
        if self.mstack:
            return self.mstack[-1]

    
    
        