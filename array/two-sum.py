class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums [j] == target: 
                    return [i,j]
        return [] 

# 我们遍历 j 的时候，是从 i+1 开始的，不能从 i 开始，因为不能重复使用同一个元素 