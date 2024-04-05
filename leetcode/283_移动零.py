from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # fast和slow移动条件不同，当nums[fast]==0时，只有fast往前移动1格
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
        for i in range(slow, fast):
            nums[i] = 0
        return
