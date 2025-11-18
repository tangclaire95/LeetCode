class Solution(object):
    def minSubArrayLen(self, target, nums):
        n=len(nums)
        ans= n+1
        s=0
        left=0
        for right, x in enumerate (nums):
            s += x
        #单调性，双指针
            while s >= target:
                ans= min(ans, right-left+1)
                s -= nums[left]
                left +=1
        return ans if ans <= n else 0 
#time o(n) space 