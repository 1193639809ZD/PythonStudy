# @Author: eveleaf
# @Date: 2024-09-04 19:01
# @LastEditTime: 2024-09-04 19:01
# @Description: 二叉搜索

from typing import List


class Solution:
    # 遍历检索
    # def search(self, nums: List[int], target: int) -> bool:
    #     for num in nums:
    #         if num == target:
    #             return True
    #     return False

    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # 关键点：如果左右相等，继续缩小范围
            elif nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
