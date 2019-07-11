"""
LRU cache
the item that was least recently used gets evicted from the collection of items

the first item in the array is the most recently used item
the last item in the array is the least recently used item - eviction happens at the end of the array
"""


class Item(object):
	def __init__(self, key, val = None):
		assert key is not None, "key of item cannot be null"
		self.key = key
		self.val = val

from collections import deque
class LRUCache(object):
	def __init__(self, N=16):
		self.q = deque()
		self.map = {}
		self.maxsize = N

	def add(self, item):
		
		


	def get(self, key):
		if key in self.map:
			index = self.map[key]
			self.map[q[0].key] = index
			self.map[key] = 0
			q[0], q[index] = q[index], q[0]
			return q[0]


	def evict():
		if q:
			q.pop()




