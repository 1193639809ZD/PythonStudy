# @Author: eveleaf
# @Date: 2024-09-04 20:20
# @LastEditTime: 2024-09-04 20:21
# @Description:

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 将矩形转化为柱型
        # left[i][j]表示左侧连续1的个数
        left = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    left[i][j] = 0
                else:
                    if j == 0:
                        left[i][j] = 1
                    else:
                        left[i][j] = left[i][j - 1] + 1
        print(left)
        # 逐个计算柱形的最大值
        ans = 0
        for j in range(len(matrix[0])):
            height = 0
            width = len(matrix[0])
            for i in range(len(matrix)):
                if left[i][j] != 0:
                    height += 1
                    width = min(width, left[i][j])
                else:
                    height = 0
                    width = len(matrix[0])
                ans = max(ans, height * width)
        return ans


if __name__ == "__main__":
    sol = Solution()
    matrix = [["0", "0", "1"], ["1", "1", "1"]]
    print(sol.maximalRectangle(matrix))
