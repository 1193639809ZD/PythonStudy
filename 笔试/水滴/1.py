# @Author: eveleaf
# @Date: 2024-09-12 21:06
# @LastEditTime: 2024-09-12 21:07
# @Description:

# 给出两个数字a，b，a每次可以乘以一个大于1的正整数得到新的a，称这个操作为它乘，计算a是否可能通过若干次它乘得到b，如果可以，输出最多的次数，如果不能，输出-1


def max_multiplications(a, b):
    # 如果 b 小于 a 或 b % a != 0，则无法通过乘法达到 b
    if b < a:
        return -1
    count = 0

    # 当 b > a 时，我们每次尝试将 b 除以一个可以整除的数
    while b > a:
        # 找到 b 中的最小因子（大于1的数）
        found = False
        for i in range(2, b):
            if b % (a * i) == 0:
                a *= i
                count += 1
                found = True
                break
        if not found:
            return -1

    # 如果最终 b == a，则说明成功
    return count if b == a else -1


# 测试用例
print(max_multiplications(5, 40))  # 2 可以通过 乘 2，4，8，16 达到输出：3
