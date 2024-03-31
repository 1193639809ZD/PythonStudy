class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True

    # 循环便利每一个字串
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        ans = ""
        for i in range(len(s)):
            for j in range(i + max_len, len(s) + 1):
                if self.isPalindrome(s[i:j]):
                    ans = s[i:j]
                    max_len = len(ans)
        return ans




if __name__ == '__main__':
    solution = Solution()
    string = "babad"
    print(solution.longestPalindrome(string))
