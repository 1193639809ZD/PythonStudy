from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        cnt_counter = defaultdict(int)

        def check():
            for char, count in t_count.items():
                if cnt_counter[char] < count:
                    return False
            return True

        left = 0
        right = -1
        min_len = float('inf')
        ans = ''

        while right < len(s) - 1:
            right += 1
            if s[right] in t_count:
                cnt_counter[s[right]] += 1

            while check() and left <= right:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left:left + min_len]

                if s[left] in t_count:
                    cnt_counter[s[left]] -= 1
                left += 1

        return ans
