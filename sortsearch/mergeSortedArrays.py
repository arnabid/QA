"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Merge 2 sorted arrays without additional memory

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.

reference:
https://leetcode.com/problems/merge-sorted-array/description/

"""

def mergeSortedArrays(nums1, m, nums2, n):
	"""
	start storing numbers from the right end of nums1
	"""
    k = m + n - 1
    m, n = m - 1, n - 1
    while m >= 0 and n >= 0:
        if nums1[m] >= nums2[n]:
            nums1[k] = nums1[m]
            m -= 1
        else:
            nums1[k] = nums2[n]
            n -= 1
        k -= 1
    while n >= 0:
        nums1[k] = nums2[n]
        k -= 1
        n -= 1

    return nums1
