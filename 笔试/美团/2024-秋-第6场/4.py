from math import gcd
from collections import Counter


def prime_factors(n):
    factors = []  # 存储质数因子
    # 处理质数因子 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # 处理其他奇数因子
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # 如果 n 是一个大于 2 的质数
    if n > 2:
        factors.append(n)

    return factors
