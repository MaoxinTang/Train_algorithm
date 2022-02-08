class NumArray:

    def __init__(self, nums: List[int]):
        """
        ** Construct the prefx sum arrays **
		the i-th item in prefx sum arrays = the sum of 0~i-1th items in the original array
           [-2,  0,  3, -5,  2, -1] #nums
           [0,  -2, -2,  1, -4, -2, -3] #pre-fix arrays
        """
        # Initialize the array
        self.dp = [0] * (len(nums) + 1) #handling the out-of-bound question
        
        # input values
        for i in range(0, len(nums)):
          self.dp[i + 1] = self.dp[i] + nums[i]


    def sumRange(self, left: int, right: int) -> int:
        """
		** 
		Test Case
        from index 0 to 2: we need to calculate -2 + 0 + 3 = 1
        however, with dp[] we can call dp[3] - dp[0] 
        """
        return self.dp[right+1] - self.dp[left]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)