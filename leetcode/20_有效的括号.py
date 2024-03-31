class Solution:
    def isValid(self, s: str) -> bool:
        # 非偶数，直接返回无效
        if len(s) % 2 == 1:
            return False
        # 注意有括号为key，左括号为value
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack
