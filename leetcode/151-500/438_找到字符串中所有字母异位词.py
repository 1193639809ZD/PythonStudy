from collections import Counter
from typing import List


class Solution:
    # 暴力
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     p_counter = Counter(p)
    #     ans = []
    #     for i in range(len(s) - len(p) + 1):
    #         substr = s[i: i + len(p)]
    #         if Counter(substr) == p_counter:
    #             ans.append(i)
    #     return ans

    # 使用Counter当滑动窗口
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     m, n = len(s), len(p)
    #
    #     ans = []
    #     ass_dict, p = Counter(s[:n]), Counter(p)
    #
    #     if ass_dict == p:
    #         ans.append(0)
    #
    #     for i in range(m - n):
    #         ass_dict[s[i]] -= 1
    #         ass_dict[s[i + n]] += 1
    #         if ass_dict == p:
    #             ans.append(i + 1)
    #
    #     return ans

    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m, res = len(s), len(p), []
        if n < m: return res
        p_cnt = [0] * 26
        s_cnt = [0] * 26

        for i in range(m):
            p_cnt[ord(p[i]) - ord('a')] += 1

        left = 0
        for right in range(n):
            cur_right = ord(s[right]) - ord('a')
            s_cnt[cur_right] += 1
            while s_cnt[cur_right] > p_cnt[cur_right]:
                cur_left = ord(s[left]) - ord('a')
                s_cnt[cur_left] -= 1
                left += 1
            if right - left + 1 == m:
                res.append(left)
        return res
