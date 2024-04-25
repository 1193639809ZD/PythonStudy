from typing import List


class Solution:
    # 利用API实现
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     try:
    #         start = nums.index(target)
    #         nums.reverse()
    #         end = len(nums) - nums.index(target) - 1
    #         return [start, end]
    #     except ValueError:
    #         return [-1, -1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 列表为空
        if not nums:
            return [-1, -1]

        leftidx, left, right = 0, 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                leftidx = mid
                right = mid - 1
            else:
                left = mid + 1

        if nums[leftidx] == target:
            rightidx, left, right = leftidx, leftidx + 1, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target >= nums[mid]:
                    rightidx = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return [leftidx, rightidx]
        else:
            return [-1, -1]
