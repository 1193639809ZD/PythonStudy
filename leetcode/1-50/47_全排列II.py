from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(comb):
            if len(comb) == len(nums):
                res.append(comb)
                return

            for i in range(len(nums)):
                # 剪枝：如果一个元素与上一个元素相同，且上一个元素在当前循环中没有使用过，说明重复了
                if used[i] == True or (i and nums[i] == nums[i - 1] and used[i - 1] == False):
                    continue
                used[i] = True
                backtrack(comb + [nums[i]])
                used[i] = False

        nums.sort()
        res, used = [], [False] * len(nums)

        backtrack([])
        return res
