class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums3 = nums1 + nums2
        nums4 = list(set(nums3))
        print(nums4)
        nums4.sort()
        print(nums4)
        num_len = len(nums4)
        print(num_len)
        print(nums4)
        if num_len % 2 == 0:
            print('1')
            return (nums4[int(num_len / 2 - 1)] + nums4[int(num_len / 2 )]) / 2
        else:
            print('2')
            return nums4[int((num_len + 1) / 2 - 1)]


a = Solution()
print(a.findMedianSortedArrays([1,3], [2]))