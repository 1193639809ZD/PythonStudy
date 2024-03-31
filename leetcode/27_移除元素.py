from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    val = 3
    s = Solution()
    print(f"ans: {s.removeElement(nums, val)}")
