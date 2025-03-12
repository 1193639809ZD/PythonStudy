"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2024-11-09 13:53:25
lastModified:  2024-11-09 13:53:26
"""

from typing import List
import collections


# 考点：连通分量
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        if nr == 0:
            return 0

        cnt = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    cnt += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        # 网格的上下左右视为相邻
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            # 判断地址是否越界，以及是为未访问过的陆地
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return cnt
