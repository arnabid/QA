"""
Design a LRU cache with a Priority Queue

Logic:
The priority of a node in the cache is an auto incrementing number. When an item is used in the cache,
its priority is updated(increases) to the current value of the counter. When an item has to be evicted from
the cache, the item with the lowest priority (ie the one that was least recently used) is popped from the
Priority Queue.
"""

class PriorityQueue(object):
    def __init__(self):
        self.pq = [] # list of entries arranged in a heap
        self.entry_finder = {} # mapping of keys to entries
        self.REMOVED = '<removed-task>' # placeholder for a removed task
        self.counter = 0

    def add(self, node):
        """ Add a new node or update the priority of an existing node """
        if node.key in self.entry_finder:
            self.remove(node)
        self.counter += 1
        entry = [self.counter, node]
        self.entry_finder[node.key] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, node):
        """ Mark an existing node in the heap as REMOVED and delete it from the
        entry_finder.  Raise KeyError if not found. """
        entry = self.entry_finder.pop(node.key)
        entry[-1] = self.REMOVED

    def pop(self):
        """ Remove and return the lowest priority task from the heap. Raise KeyError if empty. """
        while self.pq:
            priority, node = heapq.heappop(self.pq)
            if node is not self.REMOVED:
                del self.entry_finder[node.key]
                return node
        raise KeyError('pop from an empty priority queue')


class Node():
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val

class LRUCache():
    def __init__(self):
        self.PQ = PriorityQueue()
        self.capacity = 16

    def get(self, key):
        priority, node = self.PQ.entry_finder.get(key, None)
        if node:
            self.PQ.add(node)
            return node.val
        return -1

     def set(self, key, val):
        if key in self.PQ.entry_finder:
            priority, node = self.PQ.entry_finder.get(key)
            node.val = val
            self.PQ.add(node)
        else:
            if len(self.PQ.entry_finder) >= self.capacity:
                self.PQ.pop() # evict node that was least recently used
            node = Node(key, val)
            self.PQ.add(node)

