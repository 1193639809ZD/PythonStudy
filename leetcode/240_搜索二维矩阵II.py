from typing import List


class Solution:
    # 暴力
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             if matrix[i][j] == target:
    #                 return True
    #     return False

    # 剪枝
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        cur_i, cur_j = 0, n - 1
        while cur_i < m and cur_j >= 0:
            if matrix[cur_i][cur_j] == target:
                return True
            if matrix[cur_i][cur_j] < target:
                cur_i += 1
            else:
                cur_j -= 1
        return False