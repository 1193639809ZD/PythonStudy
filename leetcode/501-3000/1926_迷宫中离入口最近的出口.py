# @Date: 2024-11-08 14:09
# @LastEditors: OBKoro1
# @LastEditTime: 2024-11-08 14:34
# @FilePath: /PythonStudy/leetcode/图论/1926_迷宫中离入口最近的出口.py


from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        print("hello")
        m, n = len(maze), len(maze[0])
        # 上下左右四个相邻坐标对应的行列变化量
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        # 入口加入队列并修改为墙
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        while q:
            cx, cy, d = q.popleft()
            # 遍历四个方向相邻坐标
            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == ".":
                    # 新坐标合法且不为墙
                    if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                        # 新坐标为出口，返回距离作为答案
                        return d + 1
                    # 新坐标为空格子且不为出口，修改为墙并加入队列
                    maze[nx][ny] = "+"
                    q.append((nx, ny, d + 1))
        # 不存在到出口的路径，返回 -1
        print("hello")
        return -1
