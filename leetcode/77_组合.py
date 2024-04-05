from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(comb, cur):
            # 回溯主体
            if len(comb) == k:
                res.append(comb)
                return
            # 回溯尝试
            # 剪枝：每个数只能用一次
            for i in range(cur, len(nums)):
                backtrack(comb + [nums[i]], i + 1)


        res, nums = [], [i for i in range(1, n + 1)]
        backtrack([], 0)
        return res