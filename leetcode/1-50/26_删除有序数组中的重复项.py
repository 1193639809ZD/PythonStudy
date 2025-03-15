from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # slow指向新元素的插入位置，也即是非重复元素的数量
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    s = Solution()
    print(f"ans: {s.removeDuplicates(nums)}")
    print(nums)
