class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def dfs(start: int):
            if start == len(nums):
                result.append([]+nums)
                return
            lookup = {}
            for i in range(start,len(nums)):
                num = nums[i]
                if num not in lookup:
                    nums[i],nums[start] = nums[start],nums[i]
                    dfs(start+1)
                    nums[i],nums[start] = nums[start],nums[i]                    
                    lookup[num] = True
                    
        dfs(0)
        return result