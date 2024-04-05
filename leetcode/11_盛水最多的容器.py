from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0

        while right > left:
            # 更新结果
            ans = max(ans, min(height[right], height[left]) * (right - left))
            # 判断左右指针如何移动
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        return ans
