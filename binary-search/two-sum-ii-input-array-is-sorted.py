class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left= 0
        right= len(numbers)-1
        while True: #left<right
            s=numbers[left]+numbers[right]
            if s== target:
                break
            if s>target:
                right -=1
            else: 
                left +=1
        return [left+1, right+1]
    

    # time o(n)
    # space o(1)
    