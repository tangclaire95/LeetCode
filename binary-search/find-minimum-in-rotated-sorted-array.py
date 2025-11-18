class Solution(object):
    def findMin(self, nums):
        # close[0,n-2]
        # open (-1, n-1)
        left= -1
        right =len(nums)-1
        while left +1 < right:
            mid =(left+right)//2
            if nums[mid] <nums[-1]: #blue
                right=mid
            else: 
                left=mid
        return nums[right]

        