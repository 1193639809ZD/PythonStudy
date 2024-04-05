class Solution:
    # deque当窗口
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     # 创建滑动窗口
    #     window = deque()
    #     # 监控窗口大小
    #     max_len = 0
    #     for i in range(len(s)):
    #         # 因为是子串，所以必须按顺序从前往后弹出元素
    #         while s[i] in window:
    #             window.popleft(0)
    #         # 添加当前字符进入滑动窗口
    #         window.append(s[i])
    #         # 如果当前窗口大小大于记录值，更新最大窗口
    #         if len(window) > max_len:
    #             max_len = len(window)
    #     return max_len

    # hash表当窗口，可以加速查找速度
    def lengthOfLongestSubstring(self, s: str) -> int:
        ass_dict, ans, left = {}, 0, -1
        for right in range(len(s)):
            if s[right] in ass_dict:
                # 更新左指针 left
                left = max(ass_dict[s[right]], left)
            # 哈希表记录
            ass_dict[s[right]] = right
            # 更新结果
            ans = max(ans, right - left)
        return ans


if __name__ == '__main__':
    in_data = "pwwkew"
    S = Solution()
    print(S.lengthOfLongestSubstring(in_data))
