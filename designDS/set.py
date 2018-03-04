"""
Design a data structure that supports the following operations on a collection of items:
add -> adds an item to the collection
remove -> removes the specified item from the collection
search -> returns the searched item from the collection if it exists; else returns Null
getRandom -> returns a random item from the collection
"""

class Item():
	def __init__(self, key = None, val = None):
		self.key = key
		self.val = val

def Set():
	def __init__(self):
		self.map = {}
		self.arr = []

	def add(self, item):
		if item.key in self.map:
			return
		n = len(self.arr)
		self.map[item.key] = n
		self.arr.append(item)

	def search(self, item):
		if item.key in self.map:
			return self.arr[self.map[item.key]]
		return None

	def getRandom(self):
		r = random.randint(0, len(self.arr)-1)
		return self.arr[r]

	def remove(self, item):
		index = self.map.get(item.key, None)
		if index is None:
			return
		last = arr[-1]
		arr[index], arr[-1] = arr[-1], arr[index]
		arr.pop()
		del self.map[item.key]
		self.map[last.key] = index

