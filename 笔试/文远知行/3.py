# @Author: eveleaf
# @Date: 2024-09-22 14:30
# @LastEditTime: 2024-09-22 14:30
# @Description:


def divide_subexpressions(nums):
    # 递归地将数组划分为子表达式
    def helper(start, end):
        # 如果只有一个元素，直接返回该元素的表达式
        if start == end:
            return [[nums[start]]]

        subexpressions = []

        # 尝试在每个位置 i 处划分
        for i in range(start, end):
            left_expressions = helper(start, i)  # 左边的子表达式
            right_expressions = helper(i + 1, end)  # 右边的子表达式

            # 合并左右表达式
            for left in left_expressions:
                for right in right_expressions:
                    subexpressions.append(left + right)

        return subexpressions

    # 获取从0到len(nums)-1的所有子表达式
    return helper(0, len(nums) - 1)


def can_make_integer(nums):
    # 递归地检查能否通过添加括号使表达式为整数
    def helper(start, end):
        # 如果只有一个数字，显然是整数
        if start == end:
            return True
        # 尝试每一种加括号的方式
        for i in range(start, end):
            left, right = nums[start : i + 1], nums[i + 1 : end + 1]
            # 检查左边能否为整数
            if helper(start, i):
                left_value = eval_expression(nums[start : i + 1])
                # 如果左边是整数，检查右边是否能整除左边
                if all(
                    left_value % eval_expression(right) == 0
                    for right in divide_subexpressions(nums[i + 1 : end + 1])
                ):
                    return True
        return False

    # 对表达式进行评估
    def eval_expression(expr):
        result = expr[0]
        for i in range(1, len(expr)):
            result /= expr[i]
        return result

    return helper(0, len(nums) - 1)


# 示例
nums = [1, 4, 2, 2]
print(can_make_integer(nums))  # 输出 True
