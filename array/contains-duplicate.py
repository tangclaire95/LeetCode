class Solution(object):
    def containsDuplicate(self, nums):
        # have an empty set, set() 是集合，特点是：不允许有重复元素。
        count = set() 
        for num in nums:
            # 如果元素已经存在，直接返回 True
            if num in count:
                return True
            # 将元素放入哈希集合
            count.add(num)
        return False

# 判断数组中是否存在重复元素
# 元素去重是哈希集合的经典应用场景，因为哈希集合可以快速地判断一个元素是否存在集合中。
# 我们可以把数组中的元素逐个放入哈希集合中，如果发现某个元素已经存在，就直接返回 true