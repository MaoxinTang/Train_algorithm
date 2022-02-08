class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArray = [1]*len(nums)
        rightArray = [1]*len(nums)
        prodArray = [1]*len(nums)
        
        for i in range(1, len(nums)):
            leftArray[i] = leftArray[i-1]*nums[i-1]
            rightArray[-i - 1] = rightArray[-i]*nums[-i]
        for i in range(len(nums)):
            prodArray[i] = leftArray[i] * rightArray[i]
            
        return prodArray