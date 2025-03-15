from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[0] * n for _ in range(n)]
        row, col, cur_dir = 0, 0, 0
        for i in range(n * n):
            res[row][col] = i + 1
            dx, dy = dirs[cur_dir]
            r, c = row + dx, col + dy
            # 需要改变方向的条件
            if r < 0 or r >= n or c < 0 or c >= n or res[r][c] > 0:
                # 顺时针旋转至下一个方向
                cur_dir = (cur_dir + 1) % 4
                dx, dy = dirs[cur_dir]
            row, col = row + dx, col + dy

        return res
