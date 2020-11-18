'''
Two Sum:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dict to store num:i
        num_to_index = {}
        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [num_to_index[target - num], i]
            else:
                num_to_index[num] = i

        return []

            
a = Solution()
x = a.twoSum([1, 2, 5, 6, 9], 8)
print(x)
x = a.twoSum([3, 3, 6, 9], 6)
print(x)
