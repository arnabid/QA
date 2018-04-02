# -*- coding: utf-8 -*-
"""
Created on Mon May 29 22:11:35 2017

@author: arnab
"""

"""
find the length of the longest consecutive sequence
reference: https://leetcode.com/problems/longest-consecutive-sequence/#/description
"""

class UF(object):
    def __init__(self, sites):
        self.id = {} # link to parent
        self.sz = {} # rank of each node
        self.count = len(sites) # number of components
        self.mx = 1

        #initialize the id and sz arrays
        for i in sites:
            self.id[i] = i
            self.sz[i] = 1

    def find(self, p):
        # returns the root of the component in which node p lies
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        # joins the 2 components in which nodes p and q lie
        proot = self.find(p)
        qroot = self.find(q)

        if proot == qroot: # do nothing
            return
        # do union by rank
        if self.sz[proot] < self.sz[qroot]:
            self.id[proot] = qroot
            self.sz[qroot] += self.sz[proot]
            self.mx = max(self.mx, self.sz[qroot])
        else:
            self.id[qroot] = proot
            self.sz[proot] += self.sz[qroot]
            self.mx = max(self.mx, self.sz[proot])
        self.count -= 1

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elements, s = set(nums), set()
        uf = UF(nums)
        for item in nums:
            if item-1 in elements and (item,item-1) not in s:
                uf.union(item, item-1)
                s.add((item, item-1))
                s.add((item-1, item))
            if item+1 in elements and (item,item+1) not in s:
                uf.union(item, item+1)
                s.add((item, item+1))
                s.add((item+1, item))
        return uf.mx
