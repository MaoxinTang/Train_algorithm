class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums + list(range(len(nums)+1)))