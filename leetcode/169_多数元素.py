from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = Counter(nums)

        for key in res:
            if res[key] > len(nums) // 2:
                return key
