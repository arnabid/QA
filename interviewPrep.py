"""
Remove Element
reference: https://leetcode.com/problems/remove-element/description/
"""

"""
Push zeros to right/left
reference: https://leetcode.com/problems/move-zeroes/description/
"""

"""
*** i is the number of elements in arr not equal to key at the end of program execution
"""
def pushkey(arr, key):
	i, j = 0, 0
	n = len(arr)
	while j < n:
		if arr[i] == key and arr[j] == key:
			j += 1
		else:
			if arr[i] == key and arr[j] != key:
				arr[i], arr[j] = arr[j], arr[i]
			i += 1
			j += 1
	return arr
