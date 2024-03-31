from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        # count 表示新鲜橘子的数量
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        # round 表示腐烂的轮数，或者分钟数
        round = 0
        # 循环结束条件
        while count > 0 and len(queue) > 0:
            round += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        count -= 1
                        queue.append((x, y))

        if count > 0:
            return -1
        else:
            return round
