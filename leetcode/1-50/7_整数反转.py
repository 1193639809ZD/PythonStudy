class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            ans = int('-' + str(x)[-1:0:-1])
        else:
            ans = int(str(x)[::-1])

        if ans < -2147483648 or ans > 2147483647:
            return 0
        else:
            return ans


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-12232134143))
