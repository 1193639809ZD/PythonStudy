"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2024-11-09 13:17:33
lastModified:  2024-11-09 13:17:33
"""

from typing import List
from collections import deque


# 考点：BFS、表格转图
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        # distances表示从(0,0)起点到(i,j)的步数，也就是距离
        distances = [[float("inf")] * n for _ in range(n)]
        distances[0][0] = 1
        queue = deque([(0, 0)])
        while queue:
            x, y = queue.popleft()
            if x == y == n - 1:
                return distances[x][y]
            # 枚举9宫格，8个方向
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    # 越界
                    if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n:
                        continue
                    # 单元格值不为0或已被访问，因为距离是按照访问的顺序计算的，所以下一个点如果小于当前点+1，就说明已经访问过了
                    if grid[x + dx][y + dy] == 1 or distances[x + dx][y + dy] <= distances[x][y] + 1:
                        continue
                    distances[x + dx][y + dy] = distances[x][y] + 1
                    queue.append((x + dx, y + dy))
        return -1
