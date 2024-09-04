# @Author: eveleaf
# @Date: 2024-07-12 09:15
# @LastEditTime: 2024-09-04 16:43
# @Description: 快慢指针

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 初始化：因为下标0的位置可能变动，因此初始化为0
        fast = slow = 0

        # 循环：fast表示待判断位置，数组全部元素均为有效范围
        while fast < len(nums):
            # 慢指针活动：慢指针表示有效元素保存的位置，只有当元素有效时，才需要移动
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            # 快指针活动
            fast += 1

        for i in range(slow, fast):
            nums[i] = 0

        return
