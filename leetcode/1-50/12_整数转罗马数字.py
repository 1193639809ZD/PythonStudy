class Solution:
    def intToRoman(self, num: int) -> str:
        # 辅助字典，注意顺序是从大到小，以及可能的组合字符
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
        ans = str()
        for key in ass_dict:
            while (num >= ass_dict[key]):
                ans = ans + key
                num = num - ass_dict[key]
        return ans
