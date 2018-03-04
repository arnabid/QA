"""
Logic:
The "number of times" a node is used is the priority of that node in the PriorityQueue(min heap).
When the PQ is full and a new element has to be added; room is made by evicting the element with
the least priority (ie the element that was least frequently used)

Each entry in the heap is a 3-element list: [priority, entry_count, node]
The entry_count acts as a tie-breaker so that two nodes with the same priority(used same # times)
are evicted in the same order they were added.

entry_finder is a dictionary: node.key -> [node.count, node]

"""


class PriorityQueue(object):
    def __init__(self):
        self.pq = [] # list of entries arranged in a heap
        self.entry_finder = {} # mapping of keys to entries
        self.REMOVED = '<removed-task>' # placeholder for a removed task
        self.counter = 0

    def add(self, node, priority=1):
        """ Add a new node or update the priority of an existing node """
        if node.key in self.entry_finder:
            self.remove(node)
        self.counter += 1
        entry = [priority, self.counter, node]
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
        self.count = 1 # number of times this node was used

class LFUCache():
    def __init__(self):
        self.PQ = PriorityQueue()
        self.capacity = 16

    def get(self, key):
        d1, d2, node = self.PQ.entry_finder.get(key, None) # d1, d2 -> dummy values
        if node:
            # this node was accessed, increment its count and add to PQ
            node.count += 1
            self.PQ.add(node, node.count)
            return node.val
        return -1


    def set(self, key, val):
        if key in self.PQ.entry_finder:
            d1, d2, node = self.PQ.entry_finder.get(key)
            node.val = val
            node.count += 1
            self.PQ.add(node, node.count)
        else:
            if len(self.PQ.entry_finder) >= self.capacity:
                self.PQ.pop() # evict node that was least frequently used
            node = Node(key, val)
            self.PQ.add(node, node.count)


