# @Author: eveleaf
# @Date: 2024-09-13 09:35
# @LastEditTime: 2024-09-13 09:35
# @Description:

from math import sqrt

# 题目：将长度为n的字符串，从左到右，从上到下，按顺序平铺成一个矩阵。矩阵的权值为这个矩阵的连通块数量。定义上下左右四个方向相邻且相同的字符是连通的。求解生成矩阵的最小权值。


# 深度优先搜索 (DFS) 计算连通块
def dfs(matrix, visited, x, y, i, j, char):
    if i < 0 or i >= x or j < 0 or j >= y or visited[i][j] or matrix[i][j] != char:
        return
    visited[i][j] = True
    # 四个方向进行 DFS 搜索
    dfs(matrix, visited, x, y, i + 1, j, char)
    dfs(matrix, visited, x, y, i - 1, j, char)
    dfs(matrix, visited, x, y, i, j + 1, char)
    dfs(matrix, visited, x, y, i, j - 1, char)


# 计算连通块的数量
def count_connected_components(matrix, x, y):
    visited = [[False] * y for _ in range(x)]
    components = 0
    for i in range(x):
        for j in range(y):
            if not visited[i][j]:  # 遍历未访问过的点
                dfs(matrix, visited, x, y, i, j, matrix[i][j])
                components += 1
    return components


# 主函数：枚举所有可能的矩阵形状，并计算最小连通块数
def min_matrix_weight(s):
    n = len(s)
    min_weight = float("inf")

    # 枚举所有可能的矩阵形状
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            y = n // x  # 保证 x * y = n

            # 构建 x 行 y 列的矩阵
            matrix = []
            for i in range(x):
                matrix.append(list(s[i * y : (i + 1) * y]))  # 将字符串按行填充到矩阵

            # 计算连通块数量
            weight = count_connected_components(matrix, x, y)
            min_weight = min(min_weight, weight)

    return min_weight


# 示例
s = "kmnplvqksghziolcfczxpygfiahpgqdaezyjmbwvwgotojprgoqjyeajlqjzrcxd"  # 可以过部分暴力解，这个过不了
print(min_matrix_weight(s))  # 输出最小权值
