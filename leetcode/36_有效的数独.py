from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)]
        column_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)]
        block_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if not c.isdigit():
                    continue
                # 获取索引
                index = int(c) - 1
                # 检测每行每列是否重复
                if row_matrix[i][index] or column_matrix[j][index] or block_matrix[(i // 3) * 3 + j // 3][index]:
                    return False
                else:
                    row_matrix[i][index] = column_matrix[j][index] = block_matrix[(i // 3) * 3 + j // 3][index] = 1
        return True
