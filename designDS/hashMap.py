"""
design a hashmap or dictionary
"""

class Item():
	def __init__(self, key = None, val = None):
		self.key = key
		self.val = val
		self.next = None


class HashMap():
	def __init__(self):
		self.size = 16
		self.arr = [None] * self.size


	def get(self, key):
		hash = abs(hash(key)) % self.size
		item = self.arr[hash]
		while item:
			if item.key == key:
				return item.val
			item = item.next
		return None


	def set(self, key, val):
		hash = abs(hash(key)) % self.size
		item = self.arr[hash]
		if item:
			prev = None
			while item:
				if item.key == key:
					item.val = val
					return
				prev = item
				item = item.next
			prev.next = Item(key, val)
		else:
			self.arr[hash] = Item(key, val)


	def remove(self, key):
		hash = abs(hash(key)) % self.size
		item = self.arr[hash]

		prev = None
		while item:
			if item.key == key:
				if prev is None:
					self.arr[hash] = item.next
				else:
					prev.next = item.next
				item.next = None
				return
			prev = item
			item = item.next

