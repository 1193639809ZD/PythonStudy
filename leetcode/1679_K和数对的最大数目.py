# @Author: eveleaf
# @Date: 2024-09-04 17:53
# @LastEditTime: 2024-09-04 17:53
# @Description:

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left, right = 0, len(nums) - 1

        res = 0
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                res += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxOperations([3, 1, 3, 4, 3], 6))
