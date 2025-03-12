"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2025-03-07 16:01:19
lastModified:  2025-03-07 16:01:19
"""


def sort_by_prefix_balance(s):
    n = len(s)
    # 计算每个位置的前缀平衡值，并记录位置索引
    prefix_balance = [(0, 1, s[0])]
    balance = 0
    for i in range(1, n):
        if s[i] == "(":
            balance += 1
        else:  # s[i] == ')'
            balance -= 1
        prefix_balance.append((balance, i + 1, s[i]))

    print(f"前缀平衡值: {prefix_balance}")

    # 按规则排序：前缀平衡值从小到大，若相同则索引从大到小
    prefix_balance.sort(key=lambda x: (x[0], -x[1]))

    # 提取排序后的括号序列
    sorted_seq = [item[2] for item in prefix_balance]
    return "".join(sorted_seq)


# 测试函数
def test_sorting(s):
    print(f"原始序列: {s}")
    result = sort_by_prefix_balance(s)
    print(f"排序后序列: {result}")
    print()


# 测试用例
test_cases = ["(()(()))", "()()"]

for case in test_cases:
    test_sorting(case)
