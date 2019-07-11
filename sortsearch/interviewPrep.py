"""
Binary search questions
"""

"""
koko eating bananas
reference: https://leetcode.com/problems/koko-eating-bananas/description/
"""

def findMinK(piles, H):
	def isPossible(k):
		return sum(math.ceil(p/k) for p in piles) <= H

	l, h = 1, max(piles)
	while l <= h:
		k = l + (h-l)//2
		if isPossible(k):
			h = k - 1
		else:
			l = k + 1
	return l

