# @Author: eveleaf
# @Date: 2024-09-04 16:56
# @LastEditTime: 2024-09-04 16:56
# @Description:


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "":
            return True

        fast = slow = 0

        while fast < len(t):
            if s[slow] == t[fast]:
                slow += 1

            fast += 1

            if slow >= len(s):
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc"))
