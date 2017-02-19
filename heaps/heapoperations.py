# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 09:52:14 2016

@author: H138576
"""

import heapq
import itertools

pq = []
entry_finder = {}
REMOVED = '<removed-task>'
counter = itertools.count()


def add_task(task, priority=0):
    """ Add a new task or update the priority of an existing task """
    if task in entry_finder:
        remove_task(task)

    count = next(counter)
    entry = [task, count, priority]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    """ Mark an existing task in the heap as removed, and delete it from the 
    entry_finder """
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    """ Remove and return the lowest priority task from the heap.
    Raise KeyError if heap is empty """
    
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

if __name__ == '__main__':
    heap = []
    data = [2, 10, 6, 7, 4, 1, 5, 3, 9, 8]
    #data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    #data = [(4,1,'N'), (3,2,'H'), (3,3,'A'), (1,4,'J'), (2,5,'O')]
    
    # build the heap
#    for item in data:
#        heappush(heap, item)
    
    heapq.heapify(data)
    
    # print some heap items
    print (heap)
    print (data)
    # empty the heap
#    ordered = []
#    while heap:
#        ordered.append(heappop(heap))
#    
#    print (ordered) # not stable
#    data.sort(key = lambda x: x[0]) # stable
#    print (data)
#    
#    print (ordered == data)
#    
