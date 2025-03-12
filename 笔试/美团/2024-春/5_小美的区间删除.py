# @Author: eveleaf
# @Date: 2024-09-12 22:03
# @LastEditTime: 2024-09-12 22:09
# @Description: 前缀和、动态规划


# 题目：小美拿到了一个大小为n的数组，她希望删除一个区间后，使得剩余所有元素的乘积末尾至少有k个0。小美想知道，一共有多少种不同的删除方案？


# 计算nums的2和5的因子数量
def count_factors(num):
    count_2 = 0
    count_5 = 0

    while num % 2 == 0:
        count_2 += 1
        num //= 2

    while num % 5 == 0:
        count_5 += 1
        num //= 5

    return count_2, count_5


def count_schemes(nums, k):
    n = len(nums)
    count_2 = [0] * (n + 1)
    count_5 = [0] * (n + 1)

    # 计算前缀和
    for i in range(n):
        c2, c5 = count_factors(nums[i])
        count_2[i + 1] = count_2[i] + c2
        count_5[i + 1] = count_5[i] + c5

    schemes = 0

    # 遍历所有可能的区间
    for start in range(n):
        for end in range(start, n):
            # 计算删除区间 [start, end] 后剩余元素的因子数量
            remaining_2 = count_2[n] - (count_2[end + 1] - count_2[start])
            remaining_5 = count_5[n] - (count_5[end + 1] - count_5[start])

            # 检查剩余元素中的 2 和 5 的因子数量是否都大于等于 k
            if remaining_2 >= k and remaining_5 >= k:
                schemes += 1

    return schemes


# 示例
# nums = [2, 5, 3, 4, 20]
# k = 2


n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(count_schemes(nums, k))  # 输出: 7
