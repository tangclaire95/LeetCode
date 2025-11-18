class Solution(object):
    def search(self, nums, target):
        def blue(i):
            end=nums[-1]
            if nums[i]>end: 
                return target > end and nums[i] >= target
            else:   
                return target > end or nums[i] >= target

        # [0, n-1]
        # (-1, n)
        left = -1
        right =len(nums)
        while left +1 < right: 
            mid=(left+right)//2
            if blue (mid): # blue
                right= mid
            else: 
                left=mid
        
        if right ==len(nums) or nums[right] != target:
            return -1
        return right 
        