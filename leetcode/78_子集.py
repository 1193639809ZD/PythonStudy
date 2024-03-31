from typing import List


class Solution:
    # 迭代
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans.extend([item + [num] for item in ans])
        return ans
