from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 左闭右闭写法
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid

        return -1
