# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         s = ""
#         for i in zip(*strs):
#             if len(set(i)) == 1:
#                 s += i[0]
#             else:
#                 break
#         return s

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]
a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))