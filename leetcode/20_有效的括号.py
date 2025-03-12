# @Author: eveleaf
# @Date: 2024-07-12 09:15
# @LastEditTime: 2024-09-28 09:11
# @Description: 栈


class Solution:
    def isValid(self, s: str) -> bool:
        # 左括号入栈，右括号匹配，出栈
        stack = []
        # 有括号和对应的左括号
        bracket = {")": "(", "]": "[", "}": "{"}

        for c in s:
            # 遇见左括号，入栈
            if c in bracket.values():
                stack.append(c)
            # 如果栈不为空，且有括号和栈顶的左括号匹配，出栈
            elif stack and bracket[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return False if stack else True
