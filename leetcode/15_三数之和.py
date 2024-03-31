from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()

        n = len(nums)
        for first in range(n):
            third = n - 1
            # 第二次开始不能重复
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, n):
                # 同first，第二次开始不能重复
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while third > second:
                    if nums[first] + nums[second] + nums[third] > 0:
                        third = third - 1
                    elif nums[first] + nums[second] + nums[third] == 0:
                        ans.append([nums[first], nums[second], nums[third]])
                        break
                    else:
                        break
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
