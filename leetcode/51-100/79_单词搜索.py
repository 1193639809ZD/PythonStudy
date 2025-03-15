from typing import List


class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #
    #     def check(i: int, j: int, k: int) -> bool:
    #         if board[i][j] != word[k]:
    #             return False
    #         if k == len(word) - 1:
    #             return True
    #
    #         visited.add((i, j))
    #         result = False
    #         for di, dj in directions:
    #             newi, newj = i + di, j + dj
    #             if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
    #                 if (newi, newj) not in visited:
    #                     if check(newi, newj, k + 1):
    #                         result = True
    #                         break
    #
    #         visited.remove((i, j))
    #         return result
    #
    #     h, w = len(board), len(board[0])
    #     visited = set()
    #     for i in range(h):
    #         for j in range(w):
    #             if check(i, j, 0):
    #                 return True
    #
    #     return False

    # 回溯
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            # 剪枝
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            # 满足条件
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # 重置状态
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False
