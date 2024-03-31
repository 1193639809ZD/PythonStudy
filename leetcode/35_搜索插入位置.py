from typing import List


class Solution:
    # 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    # 二插搜索
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # '<=' 是要点，必须以 left > right 结束循环，这样最终结果分布是right-ans-left，可以减少需要讨论的情况
        while (left <= right):
            ans = (left + right) // 2
            if nums[ans] == target:
                return ans
            elif nums[ans] < target:
                left = ans + 1
            else:
                right = ans - 1
        return left


    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     try:
    #         return nums.index(target)
    #     except ValueError:
    #         nums.append(target)
    #         nums.sort()
    #         return nums.index(target)
