class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        l, r, res = 0, len(nums) - 1, 0
        nums.sort()
        
        while l < r:
            res += nums[r] - nums[l]
            l += 1
            r -= 1
        
        return res