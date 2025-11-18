class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # L, R
        # [l,r] [l+1,r], ... , [r,r]
        # R-L+1
        if k <=1:
            return 0
        ans =0
        prod =1
        left= 0
        for right, x in enumerate (nums):
            prod *=x 
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right -left +1
        return ans  