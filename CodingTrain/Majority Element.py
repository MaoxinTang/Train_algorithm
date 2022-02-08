class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=Counter(nums)
        return max(a,key=a.get)