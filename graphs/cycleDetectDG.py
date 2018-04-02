# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:22:53 2017

@author: arnab
"""

"""
cycle detection in directed graph
"""

"""
N = number of nodes in G

using BFS; find the topological sort order
if the length of the topological sort order == N; no cycle exists
else topological sort is not possible and therefore 
G must contain a cycle.

refer to: https://leetcode.com/problems/course-schedule/#/description
"""