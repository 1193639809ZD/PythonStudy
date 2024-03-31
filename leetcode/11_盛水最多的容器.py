from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        目标：最大化 min(height[right], height[left]) * (right - left)

        :param height:
        :return:
        """
        right = len(height) - 1
        left = 0
        ans = 0
        while right > left:
            # 更新结果
            if min(height[right], height[left]) * (right - left) > ans:
                ans = min(height[right], height[left]) * (right - left)
            # 判断左右指针如何移动
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea(121))
