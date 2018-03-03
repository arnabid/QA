# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:05:16 2017

@author: arnab
"""

"""
Design a simple cache; eviction policy is to remove a random element
"""
import random

class SimpleCache():
    def __init__(self):
        self.maxsize = 16
        self.cache = {}
    
    # gets the value associated with key in cache; else returns None
    def get(self, key):
        return self.cache.get(key, None)

    # adds entry (key, value) in cache
    def add(self, key, value):
        # if cache is full, delete random entry in cache
        if len(self.cache) == self.maxsize:
            rkey = random.choice(list(self.cache.keys()))
            del self.cache[rkey]

        # insert new element in cache
        self.cache[key] = value
    
    # returns the size of cache
    def size(self):
        return len(self.cache)
