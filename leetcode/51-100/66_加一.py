from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 1:
                digits[i] += carry
                carry = digits[i] // 10
                digits[i] = digits[i] % 10
            else:
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits

    # 调用库函数
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     res = eval(''.join(map(str, digits))) + 1
    #     return list(map(int, str(res)))


if __name__ == '__main__':
    digits = [1, 9, 9]
    solution = Solution()
    print(solution.plusOne(digits))
