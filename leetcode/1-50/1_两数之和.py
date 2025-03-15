# @Author: eveleaf eveleaf@outlook.com.ar
# @Date: 2024-07-12 09:15
# @LastEditors: eveleaf eveleaf@outlook.com.ar
# @LastEditTime: 2024-11-08 14:16
# @FilePath: /leetcode/1_两数之和.py

from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 将所有元素存入hash表，key为元素，value为下标
        ass_dict = {}
        for i in range(len(nums)):
            ass_dict[nums[i]] = i
        # 遍历数组，查找hash表中是否存在key=target-nums[i]
        for i in range(len(nums)):
            j = ass_dict.get(target - nums[i])
            if j and i != j:
                return [i, j]

    #
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print("test")
    print(f"nums: {nums}")
    print(f"target: {target}")
    print(f"answer: {s.twoSum(nums=nums, target=target)}")
