class Solution(object):
    def trap(self, height):
        n=len(height)
        ans=0
        left=0
        right=n-1
        pre_max=0 #前缀最大值
        suf_max=0 #后缀最大值
        while left <= right:
            pre_max=max (pre_max, height[left])
            suf_max=max (suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else: 
                ans += suf_max -height[right]
                right -=1
        return ans 


