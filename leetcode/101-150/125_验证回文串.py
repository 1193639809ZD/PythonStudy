"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2025-03-14 19:16:08
lastModified:  2025-03-14 19:16:10
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char.lower() for char in s if char.isalpha()])

        return s == s[::-1]
