from typing import List


class Solution:
    # 迭代
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(comb, cur):
            # 回溯主体
            res.append(comb)
            # 回溯尝试
            for i in range(cur, len(nums)):
                # 剪枝：重复起点跳过
                if i and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue

                used[i] = True
                backtrack(comb + [nums[i]], i + 1)
                # 重置状态
                used[i] = False

        # 候选项排序
        nums.sort()

        res, used = [], [False] * len(nums)
        backtrack([], 0)
        return res
