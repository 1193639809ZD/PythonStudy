# @Author: eveleaf
# @Date: 2024-09-13 09:06
# @LastEditTime: 2024-09-13 09:10
# @Description: 前缀和

# 题目：有一个n行m列的二维数组，可以横着或者竖着，切成两个新的二维数值s1、s2，输出s1、s2之和的最小差值。


def min_diff_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # 特判，如果只有一行一列，直接返回该元素
    if n == 1 and m == 1:
        return matrix[0][0]

    # 计算二维数组的前缀和
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] = (
                matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
            )

    total_sum = prefix_sum[n][m]  # 整个矩阵的和
    min_diff = float("inf")  # 初始化最小差值为无穷大

    # 横向切割
    for i in range(1, n):
        s1 = prefix_sum[i][m]  # 上半部分的和
        s2 = total_sum - s1  # 下半部分的和
        min_diff = min(min_diff, abs(s1 - s2))

    # 竖向切割
    for j in range(1, m):
        s1 = prefix_sum[n][j]  # 左半部分的和
        s2 = total_sum - s1  # 右半部分的和
        min_diff = min(min_diff, abs(s1 - s2))

    return min_diff


# 示例
matrix = [[1]]

print(min_diff_sum(matrix))  # 输出最小差值
