from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            ans[key].append(st)

        return list(ans.values())
