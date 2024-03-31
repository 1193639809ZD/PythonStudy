from typing import List


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    s = Solution()
    print(f"nums: {nums}")
    print(f"target: {target}")
    print(f"answer: {s.twoSum(nums=nums, target=target)}")
