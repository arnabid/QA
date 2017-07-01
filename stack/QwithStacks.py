# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 17:06:45 2017

@author: arnab
"""

"""
Design a queue using stacks
"""

class Q_Using_Stacks(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, x):
        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.s2.append(x)
            while self.s2:
                self.s1.append(self.s2.pop())
        else:
            self.s1.append(x)
    
    def deque(self):
        if self.s1:
            return self.s1[-1]
