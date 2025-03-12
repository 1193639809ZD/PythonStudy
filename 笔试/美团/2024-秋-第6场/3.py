def max_sets(a, b, c, x, y):
    # 初始化 dp 数组
    dp = [[[0 for _ in range(c + 1)] for _ in range(b + 1)] for _ in range(a + 1)]

    # 状态转移方程
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                # 不进行合成的情况
                dp[i][j][k] = min(i, j, k)

                # 尝试用红砖合成蓝砖
                if i >= x and j + 1 <= b:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - x][j + 1][k])

                # 尝试用蓝砖合成绿砖
                if j >= y and k + 1 <= c:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - y][k + 1])

    return dp[a][b][c]


# 示例输入
a = 10  # 红砖数量
b = 2  # 蓝砖数量
c = 1  # 绿砖数量
x = 4  # 每x块红砖合成1块蓝砖
y = 2  # 每y块蓝砖合成1块绿砖

# 调用函数计算结果
result = max_sets(a, b, c, x, y)
print(result)  # 输出结果
