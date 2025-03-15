from typing import List


class Solution:
    # 循环遍历
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     ans = []
    #     for i in range(len(temperatures)):
    #         find = False
    #         for j in range(i + 1, len(temperatures)):
    #             if temperatures[j] > temperatures[i]:
    #                 ans.append(j - i)
    #                 find = True
    #                 break
    #         if not find:
    #             ans.append(0)
    #     return ans

    # 单调栈
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                pre_index = stack.pop()
                ans[pre_index] = i - pre_index
            stack.append(i)
        return ans
