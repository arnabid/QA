"""
find the number of subsets of a set of numbers that sum to K
"""

# returns the number of subsets of arr[i:] that sum to total
def countsubsetsK(arr, total, i, mem):
	key = (total, i)

	#use memoization
	if key in mem:
		return mem[key]

	if total == 0:
		return 1

	# no more elements to choose
	if i == len(arr):
		return 0

	if arr[i] > total:
		res = countsubsetsK(arr, total, i+1, mem)
	else:
		res = countsubsetsK(arr, total, i+1, mem) + countsubsetsK(arr, total-arr[i], i+1, mem)
	mem[key] = res
	return res


if __name__ == '__main__':
	arr = [5,2,7]
	K = 7
	mem = {}
	print (countsubsetsK(arr, K, 0, mem))
	print (mem)