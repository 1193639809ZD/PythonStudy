from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 将排序后的子串作为key，存入hash表中
        ans = defaultdict(list)

        for s in strs:
            temp = "".join(sorted(s))
            ans[temp].append(s)

        return list(ans.values())
