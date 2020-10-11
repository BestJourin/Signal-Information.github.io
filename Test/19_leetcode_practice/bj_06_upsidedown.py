class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(abs(x))
        if x < 0: num = -int(str_num[::-1])
        else:num = int(str_num[::-1])
        if num > -2 ** 31 and num < 2 ** 31 - 1: return num
        else:return 0

a = Solution()
print(a.reverse(-1324354))