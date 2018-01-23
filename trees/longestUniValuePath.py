"""
Given a binary tree, find the length of the longest path where each node in the path has the same value.
This path may or may not pass through the root.

reference: https://leetcode.com/problems/longest-univalue-path/description/
"""

ans = [0]

def findLongestUniValuePath(root):
	findLongestUniValuePathUtil(root)
	return ans[0]

def findLongestUniValuePathUtil(root):
	if root is None:
		return 0

	lv, rv, res = 0, 0, 0
	if root.left:
		lv = findLongestUniValuePathUtil(root.left)
		if root.val == root.left.val:
			ans[0] = max(ans[0], lv + 1)
			res = max(res, lv + 1)
	if root.right:
		rv = findLongestUniValuePathUtil(root.right)
		if root.val == root.right.val:
			ans[0] = max(ans[0], rv + 1)
			res = max(res, rv + 1)
	if root.left and root.right:
		if root.val == root.left.val and root.val == root.right.val:
			ans[0] = max(ans[0], lv + rv + 2)
			res = max(res, max(lv,rv) + 1)
	return res