from itertools import permutations
class Solution:
    def invalid(self, x):
        n = len(x)
        flag = False
        for i in range(n):
            if flag: break
            for j in range(i+2, n):
                if flag: break
                for k in range(i+1, j):
                    if 2*x[k] == x[i]+x[j]: flag = True; break
        return flag
        
    def beautifulArray(self, n: int) -> List[int]:
        for perm in permutations(range(1, n+1)):
            if not self.invalid(perm):
                return perm

class Solution:
    def recurse(self, nums):
        if len(nums) <= 2: return nums
        return self.recurse(nums[::2]) + self.recurse(nums[1::2])
    
    def beautifulArray(self, n: int) -> List[int]:
        return self.recurse([i for i in range(1, n+1)])


Solution_link: https://leetcode.com/problems/beautiful-array/discuss/1368125/Detailed-Explanation-with-Diagrams.-A-Collection-of-Ideas-from-Multiple-Posts.-Python3