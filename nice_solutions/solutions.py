"""
Move zeros to the right of an array while maintaining the relative ordering
of the non-zero elements in the array.
Reference: https://leetcode.com/problems/move-zeroes/
solution description: maintain insert_position index;
if arr[i] != 0; swap (insert_position, i)
increment i, increment insert_position
"""

from typing import List

def moveZeroes(nums: List[int]) -> None:
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1


"""
Dutch flag sorting - without using the sort routine and in one pass
Reference: https://leetcode.com/problems/sort-colors/
l = insertion point of 0 (beginning of array)
h = insertion point of 2 (end of the array)
m = current index being evaluated
insight: only 2 position indices needed to sort 3 colors
"""

def sortColors(self, nums: List[int]) -> List[int]:
    n = len(nums)
    l, m, h = 0, 0, n-1
    while m <= h:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            l += 1
            m += 1
        elif nums[m] == 2:
            nums[h], nums[m] = nums[m], nums[h]
            h -= 1
        else:
            m += 1
    return nums

