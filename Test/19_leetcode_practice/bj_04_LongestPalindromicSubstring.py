class Solution:
    def longestPalindrome(self, s: str) -> str:
        # manacher法专门用来解决回文字符串的问题
        start = 0
        if len(s) < 2:
            return s
        # 将一个可能是偶数长/奇数长的字符串，首位以及每个字符间添加#
        test = '#' + '#'.join(s) + '#'
        # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
        max_len = 0
        for i in range(len(test)):
            left = i - 1
            right = i + 1
            step = 0
            # print(test[i])
            while left >= 0 and right < len(test) and test[left] == test[right]:
                # print("spread",test[left],test[right])
                left -= 1
                right += 1
                step += 1
                # print(step)

            if step > max_len:
                max_len = step
                start = (i - max_len) // 2
        return s[start: start + max_len]
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         max_len = 0
#         start = 0
#         if len(s) < 2:
#             return s
#         for i in range(len(s)):
#             left = i - 1
#             right = i + 1
#             str_len = 1
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#                 str_len += 2
#             if left >= 0 and right < len(s) and s[left] == s[i] and s[right] != s[i]:
#                 left -= 1
#                 str_len += 1
#             elif left >= 0 and right < len(s) and s[left] != s[i] and s[right] == s[i]:
#                 str_len += 1
#             if str_len > max_len:
#                 max_len = str_len
#                 start = left + 1
#         return s[start: start + max_len]


question = Solution()
print(question.longestPalindrome("babad"))