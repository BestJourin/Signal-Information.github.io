import time
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in res: res.append([nums[i], nums[j], nums[k]])

        return res
print(time.time())
a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))
print(time.time())