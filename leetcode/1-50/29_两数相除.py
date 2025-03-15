class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = int(dividend / divisor)
        if ans > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif ans < -pow(2, 31):
            return -pow(2, 31)
        else:
            return ans
