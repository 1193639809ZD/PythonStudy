class Solution:
    def decodeString(self, s: str) -> str:
        queue, ans, count = list(), "", 0

        for c in s:
            if c.isalpha():
                ans += c
            elif c.isdigit():
                count = count * 10 + int(c)
            elif c == "[":
                queue.append((ans, count))
                ans, count = "", 0
            else:
                sub, cnt = queue.pop()
                ans = sub + ans * cnt
        return ans
