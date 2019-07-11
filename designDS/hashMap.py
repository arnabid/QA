"""
design a hashmap or dictionary
"""

class Item():
	def __init__(self, key, val = None):
		assert key is not None, "key of item cannot be null"
		self.key = key
		self.val = val
		self.next = None


class HashMap():
	def __init__(self):
		self.size = 16
		self.arr = [None] * self.size


	def get(self, key):
		h = abs(hash(key)) % self.size
		item = self.arr[h]
		while item:
			if item.key == key:
				return item.val
			item = item.next
		return None


	def set(self, key, val):
		h = abs(hash(key)) % self.size
		item = self.arr[h]
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
			self.arr[h] = Item(key, val)


	def remove(self, key):
		h = abs(hash(key)) % self.size
		item = self.arr[h]

		prev = None
		while item:
			if item.key == key:
				if prev is None:
					self.arr[h] = item.next
				else:
					prev.next = item.next
				item.next = None
				return
			prev = item
			item = item.next

