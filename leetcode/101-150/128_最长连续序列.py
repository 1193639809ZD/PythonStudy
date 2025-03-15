from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ass_set = set(nums)

        ans = 0
        # 直接遍历过滤掉重复数值的集合即可
        for num in ass_set:
            # 从最小连续值开始计算
            if num - 1 not in ass_set:
                target = num
                cnt = 1
                while target + 1 in ass_set:
                    target += 1
                    cnt += 1
                ans = max(ans, cnt)
        return ans

    # 哈希表方式一
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #
    #     nums.sort()
    #
    #     ans = defaultdict(int)
    #     for i in range(len(nums)):
    #         if i and nums[i] == nums[i - 1]:
    #             continue
    #         ans[nums[i]] = ans[nums[i] - 1] + 1
    #     return max(ans.values())
