# @Author: eveleaf
# @Date: 2024-08-29 14:14
# @LastEditTime: 2024-09-03 14:52
# @Description:

# @Author: eveleaf
# @Date: 2024-08-29 14:14
# @LastEditTime: 2024-08-29 14:14
# @Description: 平方根计算

import math


class Solution:
    # def mySqrt(self, x: int) -> int:
    #     # 要求：返回平方根的整数部分
    #     return int(pow(x, 0.5))

    # 模拟
    # def mySqrt(self, x: int) -> int:
    #     if x == 0:
    #         return 0
    #     if x == 1 or x == 2:
    #         return 1

    #     for i in range(x):
    #         if i * i == x:
    #             return i
    #         if i * i > x:
    #             return i - 1

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))
