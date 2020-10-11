class Solution:
    @classmethod
    def lengthOfLongestSubstring(cls, s: str) -> int:
        s_len = len(s)
        str_index = dict()
        start = end = max_len = 0
        while end < s_len:
            if str_index.get(s[end], -1) >= start:
                max_len = max(end - start, max_len)
                start = str_index[s[end]] + 1
            str_index[s[end]] = end
            end += 1
        return max(max_len, end - start)
print(Solution.lengthOfLongestSubstring("abdasdadw"))