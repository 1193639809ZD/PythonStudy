# @Author: eveleaf
# @Date: 2024-09-22 14:07
# @LastEditTime: 2024-09-22 14:08
# @Description:

# 题目：给定一个n个整数构成的数组a，满足a1+a2+...+an = 0。每次操作，选择下标i，j，将ai减1，aj加1，如果i<j无消耗，反之，消耗1，问需要消耗多少才能使所有元素均变为0


def min_cost_to_balance(a):
    accumulation = 0
    cost = 0
    for i in range(len(a)):
        accumulation += a[i]
        # 如果累计和为负，需要从后面的正数往前移动，产生消耗
        if accumulation < 0:
            cost += -accumulation  # 负值越多，消耗越多
            accumulation = 0
    return cost


# 示例
a = [-3, 2, -3, 4]
print(min_cost_to_balance(a))  # 输出最小消耗
