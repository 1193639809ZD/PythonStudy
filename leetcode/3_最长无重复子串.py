class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        function: 给定一个字符串s，请你找出其中不含有重复字符的最长子串的长度
        :param s:
        :return:
        """
        # 创建滑动窗口
        window = list()
        # 监控窗口大小
        max_len = 0
        for i in range(len(s)):
            while s[i] in window:
                window.pop(0)
            # 添加当前字符进入滑动窗口
            window.append(s[i])
            # 如果当前窗口大小大于记录值，更新最大窗口
            if len(window) > max_len:
                max_len = len(window)
        return max_len


if __name__ == '__main__':
    in_data = "pwwkew"
    S = Solution()
    print(S.lengthOfLongestSubstring(in_data))