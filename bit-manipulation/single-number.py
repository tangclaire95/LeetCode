class Solution(object):
    def singleNumber(self, nums):
        count={}
        # 遍历数组，统计每个数字出现的次数
        for num in nums:
            count[num]=count.get(num,0) +1 
    
      # 找到只出现一次的数字
        for num in nums: 
            if count[num]==1:
                return num  
        return -1

# 找出数组中只出现一次的数字，对于元素计数相关的问题，我们一般要用键值对来存储元素和其出现次数的对应关系，也就是要用到哈希表这种数据结构。