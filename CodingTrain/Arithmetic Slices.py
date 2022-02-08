class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res, count, d = 0, 0, float('inf')

        n = len(nums)
        for i in range(1, n):
            
            if nums[i] - nums[i-1] == d:
                count += 1
            else: 
                res += count*(count+1)//2
                count = 0 
                d = nums[i]-nums[i-1]
        
        return res + count*(count+1)//2