"""
Design a data structure that supports the following operations on a collection of items:
add -> adds an item to the collection
remove -> removes the specified item from the collection
search -> returns the searched item from the collection if it exists; else returns Null
getRandom -> returns a random item from the collection

All operations have O(1) time complexity
Space complecity: O(N); N = number of items in collection
"""

class Item():
	def __init__(self, key, val = None):
		assert key is not None, "key of item cannot be null"
		self.key = key
		self.val = val

def Set():
	def __init__(self):
		self.map = {}
		self.arr = []
		self.size = 0

	# adds an item to the collection
	def add(self, item):
		if item.key in self.map:
			self.arr[self.map[item.key]] = item
			return
		self.map[item.key] = self.size
		self.arr.append(item)
		self.size += 1

	# searches for the item in the collection, return if found else return None
	def search(self, item):
		if item.key in self.map:
			return self.arr[self.map[item.key]]
		return None

	# returns a random item from the collection
	def getRandom(self):
		r = random.choice(range(0, self.size))
		return self.arr[r]

	# removes the item from the collection if it exists
	def remove(self, item):
		index = self.map.get(item.key, None)
		if index is None:
			return
		last = arr[-1]
		arr[index], arr[-1] = arr[-1], arr[index]
		arr.pop()
		self.size -= 1
		self.map[last.key] = index
		del self.map[item.key]
