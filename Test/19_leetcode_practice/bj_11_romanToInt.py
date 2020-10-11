class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4, 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res = 0
        for key in hashmap:
            if key in s:
                res += s.count(key) * hashmap[key]
                s = s.replace(key, '')
        return res

a = Solution()
print(a.romanToInt("III"))