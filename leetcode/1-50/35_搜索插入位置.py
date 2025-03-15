from typing import List


class Solution:
    # 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    # 二插搜索
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     res, left, right = len(nums), 0, len(nums) - 1
    #     # nums[pos−1] < target <= nums[pos]
    #     while left <= right:
    #         mid = (right + left) // 2
    #         # '='条件下，必须移动right
    #         if target <= nums[mid]:
    #             res = mid
    #             right = mid - 1
    #         else:
    #             left = mid + 1

    #     return res

    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            print(mid, left, right)
        return left


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 3, 5, 6]
    target = 2

    print(sol.searchInsert(nums, target))

    # print(3 // 2)
