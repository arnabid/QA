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
mstack will always be sorted in non-increasing order.
"""

class MinStack():
    def __init__(self):
        self.stack = []
        self.mstack = []
    
    def push(self, x):
        # insert x into stack
        self.stack.append(x)

        # if mstack is empty, insert x into mstack
        # if mstack is not empty, insert into mstack if x <= mstack[-1]
        if self.mstack:
            if x <= self.mstack[-1]:
                self.mstack.append(x)
        else:
            self.mstack.append(x)
    
    def pop(self):
        # check if stack is non-empty
        if self.stack:
            # if element popped is current min, pop it from mstack also
            if self.stack[-1] == self.mstack[-1]:
                self.mstack.pop()

            # pop and return top element from stack
            return self.stack.pop()
    
    def findMin(self):
        # return top element of mstack
        if self.mstack:
            return self.mstack[-1]
        else:
            return "Stack empty"

if __name__ == '__main__':
    sol = MinStack()
    sol.push(5)
    print (sol.findMin()) # 5
    sol.push(1)
    print (sol.findMin()) # 1
    print (sol.pop())     # 1
    print (sol.findMin()) # 5
    print (sol.stack)

    
    
        