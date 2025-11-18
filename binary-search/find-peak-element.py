class Solution(object):
    def findPeakElement(self, nums):
        # [0, n-2]闭区间
        # (-1, n-1)开区间
        left= -1
        right= len(nums)-1
        while left+1 < right: 
            mid=(left+right)//2
            if nums[mid] > nums[mid+1]: # blue
                right=mid
            else:
                left=mid
        return right 
# time: o(logn), space o(1)
