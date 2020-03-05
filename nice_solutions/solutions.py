"""
Move zeros to the right of an array
Reference: https://leetcode.com/problems/move-zeroes/
solution description: Do not use 2 pointers and swap values; difficult to understand 
maintain insert_position index;
if arr[i] != 0; arr[insert_position] = arr[i]
increment i, increment insert_position
"""

from typing import List

def moveZeroes(nums: List[int]) -> None:
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            if i > insert_pos:
                nums[i] = 0
            insert_pos += 1
