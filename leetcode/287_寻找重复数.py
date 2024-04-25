from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ass_set = set()

        for num in nums:
            if num not in ass_set:
                ass_set.add(num)
            else:
                return num
