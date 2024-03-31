from typing import List


class Solution:
    # 循环遍历
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     ans = 0
    #     for i in range(len(heights)):
    #         left, right = i, i
    #         while left - 1 >= 0 and heights[left - 1] >= heights[i]:
    #             left -= 1
    #         while right + 1 < len(heights) and heights[right + 1] >= heights[i]:
    #             right += 1
    #         ans = max(ans, heights[i] * (right + 1 - left))
    #     return ans

    # 使用索引列表
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     ans = 0
    #     n = len(heights)
    #     # 检索右侧第一个下降的元素与当前元素的距离
    #     ass_right = [0] * n
    #     stack = list()
    #     for i in range(n):
    #         height = heights[i]
    #         while stack and height < heights[stack[-1]]:
    #             pre_index = stack.pop()
    #             ass_right[pre_index] = i - pre_index
    #         stack.append(i)
    #     # 检索左侧第一个下降的元素与当前元素的距离
    #     ass_left = [0] * n
    #     stack.clear()
    #     for i in range(n - 1, -1, -1):
    #         height = heights[i]
    #         while stack and height < heights[stack[-1]]:
    #             pre_index = stack.pop()
    #             ass_left[pre_index] = pre_index - i
    #         stack.append(i)
    #     # 遍历
    #     for i in range(n):
    #         if ass_left[i]:
    #             left = i - ass_left[i] + 1
    #         else:
    #             left = 0
    #         if ass_right[i]:
    #             right = i + ass_right[i] - 1
    #         else:
    #             right = n - 1
    #         ans = max(ans, heights[i] * (right + 1 - left))
    #     return ans

    # 加速索引列表生成
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
