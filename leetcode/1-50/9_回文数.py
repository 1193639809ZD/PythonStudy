class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 转化为字符串，便于获取指定下标元素
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[-(i + 1)]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
