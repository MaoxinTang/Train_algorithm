class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter=1
        for i in reversed(nums):
            if(counter==k):
                return i
            counter+=1

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]