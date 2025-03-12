# @Author: eveleaf
# @Date: 2024-09-19 21:07
# @LastEditTime: 2024-09-19 21:08
# @Description:


def findContentChildren(a, b):
    # 对饥饿值数组a和饼干大小数组b排序
    a.sort()
    b.sort()

    i, j = 0, 0  # i指向饥饿值数组a，j指向饼干大小数组b
    satisfied_people = 0  # 记录被满足的人数

    # 尝试用饼干去满足每个人
    while i < len(a) and j < len(b):
        if b[j] >= a[i]:  # 当前饼干能满足当前人
            satisfied_people += 1
            i += 1  # 换下一个人
        j += 1  # 换下一个饼干

    return satisfied_people


# 测试
a = [1, 2]
b = [1, 2, 3]
print(findContentChildren(a, b))  # 输出 1
