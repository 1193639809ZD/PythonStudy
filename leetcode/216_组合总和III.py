from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(comb, cur):
            # 回溯主体
            if len(comb) == k and sum(comb) == n:
                res.append(comb)
            # 回溯尝试
            for i in range(cur, len(nums)):
                # 剪枝
                if sum(comb + [nums[i]]) > n:
                    return
                backtrack(comb + [nums[i]], i + 1)

        res, nums = [], [i for i in range(1, 10)]
        backtrack([], 0)
        return res
