class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for item in s.split(' ')[::-1]:
            if item != '':
                return len(item)
