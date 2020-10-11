class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_upsidedown = 0
        x_vib = x
        if x < 0:return False
        else:
            while(x_vib > 0):
                x_upsidedown = x_upsidedown * 10 + x_vib % 10
                x_vib //= 10
            if x_upsidedown == x:return True
            else:return False

a = Solution()
print(a.isPalindrome(1234321))