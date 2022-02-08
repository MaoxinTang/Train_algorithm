class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for num in nums:
            res ^= num
            
        rightmost_one = 1
        while not res & 1:
            res = res >> 1
            rightmost_one = rightmost_one << 1
            
        num1, num2 = 0, 0
        for num in nums:
            if (rightmost_one & num) != 0:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1, num2]