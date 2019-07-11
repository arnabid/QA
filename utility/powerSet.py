
"""
find the power set of elements in input array
"""
def print_ss(ss):
	for x in ss:
		if x:
			print (x, end=",")
	print ("")


def find_subsets1(arr):
	ss = [None] * len(arr)
	helper(arr, ss, 0)

def helper(arr, ss, i):
	"""
	make a decision on item arr[i]; either select it or not
	"""
	if i == len(arr):
		print_ss(ss)
		return

	# do not select current element arr[i]
	ss[i] = None 
	helper(arr, ss, i+1)

	# select current element arr[i]
	ss[i] = arr[i]
	helper(arr, ss, i+1)


"""
iterative solution
"""
def find_subsets2(arr):
	n = len(arr)
	ps_size = 2**n
	"""
	there are 2**n subsets, n positions (marked with n bits)
	for example the 7th position will be marked as 111 and
	then 7 & (every position will be 1) so every element will be included
	"""
	for count in range(ps_size):
		for j in range(n):
			if count & (1 << j):
				print (arr[j], end=",")
		print ("")


if __name__ == '__main__':
	arr = [2,2,3]
	find_subsets1(arr)

	find_subsets2(arr)