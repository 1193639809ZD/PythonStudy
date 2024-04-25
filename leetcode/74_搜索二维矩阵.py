from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, left, right = 0, 0, len(matrix) - 1
        # 左闭右闭写法
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[mid][0]:
                right = mid - 1
            else:
                row = mid
                left = mid + 1

        col, left, right = 0, 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True

        return False
