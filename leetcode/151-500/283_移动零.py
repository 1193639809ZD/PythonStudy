# @Author: eveleaf
# @Date: 2024-07-12 09:15
# @LastEditTime: 2024-09-04 16:43
# @Description: 快慢指针

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        不返回任何值，原地修改数据
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast]:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return
