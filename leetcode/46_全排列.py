from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(comb):
            if len(comb) == n:
                res.append(comb)
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    backtrack(comb + [nums[i]])
                    used[i] = False

        n = len(nums)
        # used的作用是防止重复读取
        res, used = [], [False] * n
        backtrack([])
        return res
