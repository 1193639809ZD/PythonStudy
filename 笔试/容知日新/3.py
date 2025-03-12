# @Author: eveleaf
# @Date: 2024-09-19 21:16
# @LastEditTime: 2024-09-19 21:16
# @Description:


def minCost(n, k, x, y):
    # dp[i] 表示将数字i变为1的最小花费
    dp = [float("inf")] * (n + 1)
    dp[1] = 0  # 将1变为1的花费是0

    for i in range(2, n + 1):
        # 考虑n = n - 1的操作
        dp[i] = dp[i - 1] + x
        # 如果i能被k整除，考虑n = n / k的操作
        if i % k == 0:
            dp[i] = min(dp[i], dp[i // k] + y)

    return dp[n]


# 测试
n = 10
k = 2
x = 1
y = 10
print(minCost(n, k, x, y))  # 输出最小花费
