from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(comb, cur):
            # 回溯主体
            res.append(comb)
            # 回溯尝试
            for i in range(cur, len(nums)):
                # 剪枝：除了起始点，重复点均跳过
                if i != cur and nums[i] == nums[i - 1]:
                    continue
                backtrack(comb + [nums[i]], i + 1)

        # 排序，防止重复
        nums.sort()

        res = []
        backtrack([], 0)
        return res
