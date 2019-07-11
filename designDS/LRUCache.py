"""
implement LRU cache
implemented using a dictionary and double linked list

The dictionary maps keys to nodes in the double linked list

Supports 2 operations:
get(key) : returns the value associated with key in the cache

set(key, value): stores the key in the cache with the associated value


The front node represents the element that was the most recently used.

Eviction takes place at the end of the linked list; the last node represents the
element that was least recently used.
"""

class Node():
	def __init__(self, key = None, val = None):
		self.key = key
		self.val = val 
		self.prev = None
		self.next = None

class LRUCache():
	def __init__(self, capacity = 16):
		self.map = {}
		self.capacity = capacity
		self.head = None
		self.end = None


	# sets the node at the front of the double linked list
	def setHead(self, node):
		if self.head:
			self.head.prev = node
			node.next = self.head
		self.head = node

		# if this node is the only element in the double linked list
		if self.end is None:
			self.end = node


	# removes the node from its current position in the double linked list
	def remove(self, node):
		# node is front node
		if node.prev is None:
			self.head = node.next
		else:
			node.prev.next = node.next

		# node is last node
		if node.next is None:
			self.end = node.prev
		else:
			node.next.prev = node.prev
		node.prev = None
		node.next = None


	# if key exists in cache, gets the value associated with key; else returns -1 
	def get(self, key):
		node = self.map.get(key, None)
		if node:
			self.remove(node)
			self.setHead(node)
			return node.val
		return -1


	# inserts new element (key, value) in cache
	def set(self, key, val):
		# key already exists in cache
		if key in self.map:
			node = self.map[key]
			node.val = val
			self.remove(node)
			self.setHead(node)
		else:
			if len(self.map) == self.capacity:
				# removes the last node in the double linked list, eviction happens here
				del self.map[self.end.key]
				self.remove(self.end)
			node = Node(key, val)
			self.map[key] = node
			self.setHead(node)
