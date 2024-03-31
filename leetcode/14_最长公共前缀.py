from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        # 取字符串列表最小长度
        n = min([len(s) for s in strs])
        # 遍历字符串列表
        for i in range(n):
            for s in strs:
                if s[i] != strs[0][i]:
                    return ans
            ans = ans + strs[0][i]
        return ans
