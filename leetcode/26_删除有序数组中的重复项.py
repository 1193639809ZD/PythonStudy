from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        # 快慢指针
        fast = slow = 1
        while fast < n:
            # 快指针每次走一步
            if nums[fast] != nums[fast - 1]:
                # 快指针走到不同元素时，更新一个慢指针
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    s = Solution()
    print(f"ans: {s.removeDuplicates(nums)}")
