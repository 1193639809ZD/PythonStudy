class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        # 状态：res[i]：第i个斐波那契数
        res = [0] * (n + 1)

        # 初始状态
        res[0], res[1] = 0, 1
        for i in range(2, n + 1):
            # 状态转移方程
            res[i] = res[i - 1] + res[i - 2]

        return res[-1]