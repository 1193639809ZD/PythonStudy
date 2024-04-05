from typing import List


class Solution:
    # 迭代
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     ans = [[]]
    #     for num in nums:
    #         ans.extend([item + [num] for item in ans])
    #     return ans
    # 回溯
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, comb):
            # 回溯尝试 & 返回条件：将temp加入res中
            res.append(comb)
            for j in range(i, n):
                backtrack(j + 1, comb + [nums[j]])

        res = []
        n = len(nums)
        backtrack(0, [])
        return res
