"""
reference: 
"""


def solution(arr, k):
	def isPossible(target):
		s = 0
		i = 0
		seg = 0
		while i < len(arr):
			if arr[i] > target: return False
			if s + arr[i] <= target:
				s += arr[i]
			else:
				s = arr[i]
				seg += 1
			i += 1
		return seg + 1 <= k

	l, h = 0, sum(arr)
	while l <= h:
		target = l + (h-l)//2
		if isPossible(target):
			h = target - 1
		else:
			l = target + 1
	return l
