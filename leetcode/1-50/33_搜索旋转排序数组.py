from typing import List


class Solution:
    # 列表API调用
    # def search(self, nums: List[int], target: int) -> int:
    #     try:
    #         return nums.index(target)
    #     except ValueError:
    #         return -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 左侧有序，注意nums[left]==nums[mid]的情况
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
