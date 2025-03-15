"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2025-03-14 15:56:46
lastModified:  2025-03-14 15:56:47
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s
