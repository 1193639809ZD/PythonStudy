class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        ass_dict = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1,
        }
        for key in ass_dict:
            while s.startswith(key):
                ans = ans + ass_dict[key]
                s = s.removeprefix(key)
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = "III"
    print(f"answer: {solution.romanToInt(s)}")
