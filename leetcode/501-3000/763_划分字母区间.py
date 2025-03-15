from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        # 记录字母最后一次出现的位置
        ass_dict = defaultdict(int)
        for i in range(len(s)):
            ass_dict[s[i]] = i
        # 子串开始的位置索引
        pre_index = -1
        # 现在遍历到的位置索引
        cur = 0
        # 目标子串截至的位置
        max_len = ass_dict[s[cur]]
        while cur < len(s):
            max_len = max(max_len, ass_dict[s[cur]])
            if cur == max_len:
                ans.append(max_len - pre_index)
                pre_index = cur
            cur += 1
        return ans
