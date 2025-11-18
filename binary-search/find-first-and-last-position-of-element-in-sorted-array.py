# 要求nums是非递减的，即nums[i] <= nums[i+1]
# 返回最小的满足 nums[i] >= target 的i
# 如果不存在，返回len(nums)

def lower_bound(nums: List[int], target: int) -> int: 
    left = 0 
    right = len(nums) - 1 # 闭区间 [left, right] 
    while left <= right: # 区间不为空 
        mid = (left + right) // 2 
        if nums[mid] < target: 
            left = mid + 1 # [mid+1, right] 
        else: right = mid - 1 # [left, mid-1] 
    return left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=lower_bound(nums,target)
        if start == len(nums) or nums[start]!=target:
            return [-1,-1]
        end= lower_bound(nums,target+1)-1
        return [start,end]
# time o(n), space o(1)

