"""
Find the element in the list that occurs odd number of times
It is guaranteed that there is only one element that occurs
odd number of times
"""


def findOddElement(arr):
	# sort the array
	arr.sort()

	i, n = 0, len(arr)
	while i < n:
		c = arr[i]
		j = i+1
		count = 1
		while j < n and a[j] == c:
			j += 1
			count += 1
		if count % 2 == 1: return c
		i = j


# time complexity - O(nlogn)
# space complexity - O(1)
def findOddElement(arr):
	# sort the array
	arr.sort()

	i, n = 0, len(arr)
	while i < n:
		cur, count = arr[i], 0
		while i < n and cur == arr[i]:
			count += 1
			i += 1
		if count % 2 != 0:
			return cur


if __name__ == '__main__':
	arr = [1]
	print (findOddElement(arr))
