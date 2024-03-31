from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            start = nums.index(target)
            nums.reverse()
            end = len(nums) - nums.index(target) - 1
            return [start, end]
        except ValueError:
            return [-1, -1]
