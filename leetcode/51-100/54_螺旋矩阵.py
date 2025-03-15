# @Author: error: git config user.name & please set dead value or install git
# @Date: 2024-08-27 11:00
# @LastEditTime: 2024-08-27 14:08
# @Description:模拟

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 方向
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        # 初始化访问矩阵
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]

        cur_x, cur_y = 0, 0
        direction_y, direction_x = directions[direction]
        res = []
        for i in range(m * n):
            res.append(matrix[cur_y][cur_x])
            visited[cur_y][cur_x] = True
            # 如果越界，或者检索到已访问地址，变换方向
            if (
                (cur_x + direction_x) < 0
                or (cur_x + direction_x) >= n
                or (cur_y + direction_y) < 0
                or (cur_y + direction_y) >= m
                or visited[cur_y + direction_y][cur_x + direction_x]
            ):
                direction = (direction + 1) % 4
                direction_y, direction_x = directions[direction]
            # 更新地址
            cur_x += direction_x
            cur_y += direction_y
        return res


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.spiralOrder(matrix))
