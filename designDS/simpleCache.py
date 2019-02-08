# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:05:16 2017

@author: arnab
"""

"""
Design a simple cache; eviction policy is to remove a randomly picked item
"""
import random

class Item(object):
    def __init__(self, key, val = None):
        assert key is not None
        self.key = key
        self.val = val

class SimpleCache(object):
    def __init__(self, N):
        self.maxsize = N
        self.cache = {}
        self.size = 0
    
    # gets the item associated with key in cache; else returns None
    def get(self, key):
        return self.cache.get(key, None)

    # adds new item in cache
    def put(self, item):
        # if cache is full, delete random item in cache
        if self.size == self.maxsize:
            self.evict()

        # insert new element in cache
        self.cache[item.key] = item
        self.size += 1
    
    # evicts a randomly chosen item from the cache 
    def evict(self):
        if self.size > 0:
            rkey = random.choice(list(self.cache.keys()))
            del self.cache[rkey]
            self.size -= 1

