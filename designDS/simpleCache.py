# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:05:16 2017

@author: arnab
"""

"""
Design a simple cache
"""
import random

class SimpleCache():
    def __init__(self):
        self.maxsize = 16
        self.cache = {}
    
    # get the value associated with key in cache
    def get(self, key):
        return self.cache.get(key, None)

    # add entry (key, value) in cache
    def add(self, key, value):
        # if cache is full, delete random entry in cache
        if len(self.cache) == self.maxsize:
            r = random.randint(0, self.maxsize-1)
            del self.cache[r]

        # insert new element in cache
        self.cache[key] = value
    
    # return the size of cache
    def size(self):
        return len(self.cache)
