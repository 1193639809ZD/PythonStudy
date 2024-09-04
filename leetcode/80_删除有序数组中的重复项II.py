# @Author: eveleaf
# @Date: 2024-09-04 15:00
# @LastEditTime: 2024-09-04 15:14
# @Description:

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 初始化：前两个元素必定有效，因此从第3个元素开始
        fast, slow = 2, 2

        while fast < len(nums):
            # 慢指针活动判断条件：也即是有效值的条件，判断nums[fast]是否已经重复了两次
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

            # 快指针
            fast += 1

        return slow


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    s = Solution()
    print(f"ans: {s.removeDuplicates(nums)}")
