class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        flage = 1
        str_num = ""
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if len(s) != 0:
            if s[0] == "-":flage = 0
            if s[0] == "-" or s[0] == "+":
                for i in s[1::]:
                    if i in num:str_num += i
                    else: break
            else:
                for i in s:
                    if i in num:str_num += i
                    else: break
            if str_num == "":return 0
            if flage == 0:number = -int(str_num)
            else:number = int(str_num)
            if number > -2 ** 31 and number < 2 ** 31 - 1:return number
            elif flage == 0:return -2 ** 31
            else:return 2 ** 31 - 1
        else: return 0


a = Solution()
print(a.myAtoi("42"))
print(a.myAtoi("   -42"))
print(a.myAtoi("4193 with words"))
print(a.myAtoi("words and 987"))
print(a.myAtoi("-91283472332"))
print(a.myAtoi(""))
print(a.myAtoi("-2147483647"))
# 方法二：
# class Solution:
#     INT_MAX = 2**31 - 1
#     INT_MIN = -2**31
#     def myAtoi(self, str: str) -> int:
#         if not str:
#             return 0
#         # 去掉空格
#         str = str.strip()
#         size = len(str)
#         i = 0
#         res = 0
#         sign = 1
#         # 首字符决定正负号
#         if i < size and (str[i] == '+' or str[i] == '-'):
#             sign = 1 if str[i] == '+' else -1
#             i += 1
#         while i < size and ('0' <= str[i] <= '9'):
#             # 先处理越界，并取10整除，因为先判断越界再做后面运算，所以要判断是否超过最大值的整除10的数
#             # res > self.INT_MAX // 10 对应最小边界
#             # res == self.INT_MAX // 10 and (ord(str[i]) - ord('0') > 7) 对应最大边界, 这里7是因为(2**31 - 1) % 10 = 7
#             if res > self.INT_MAX // 10 or (res == self.INT_MAX // 10 and (ord(str[i]) - ord('0') > 7)):
#                 if sign == 1:
#                     return self.INT_MAX
#                 else:
#                     return self.INT_MIN
#             res = res * 10 + ord(str[i]) - ord('0')
#             i += 1
#         return res * sign
