import heapq
import itertools
"""
Priority Queue implementation:
Each entry in the heap is a 3-element list: [priority, entry_count, task]
The entry count acts as a tie-breaker so that two tasks with the same priority
are returned in the same order they were added.

At any point in time, entry_finder holds only the active tasks.
The heap contains tasks which have been tagged 'REMOVED' (priority changed/removed)
and the active tasks.
"""

class PriorityQueue(object):
    def __init__(self):
        self.pq = [] # list of entries arranged in a heap
        self.entry_finder = {} # mapping of tasks to entries
        self.REMOVED = '<removed-task>' # placeholder for a removed task
        self.counter = itertools.count() # unique sequence count

    def add(self, task, priority=0):
        """ Add a new task or update the priority of an existing task """
        if task in self.entry_finder:
            self.remove(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, task):
        """ Mark an existing task in the heap as REMOVED and delete it from the
        entry_finder.  Raise KeyError if not found. """
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop(self):
        """ Remove and return the lowest priority task from the heap. Raise KeyError if empty. """
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

