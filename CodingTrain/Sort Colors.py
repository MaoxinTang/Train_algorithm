


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low = 0
        mid = 0
        high = n-1
        while mid <= high :
            if nums[mid] == 0:
                nums[mid] , nums[low] = nums[low] , nums[mid]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid] , nums[high] = nums[high] , nums[mid]
                
                high -= 1
        return nums    


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red,white,blue=0,0,0
        
        for i in range(len(nums)):
            if nums[i]==0:
                red+=1
            elif nums[i]==1:
                white+=1
            else:
                blue+=1
            
        for i in range(len(nums)):
            if i<red:
                nums[i]=0
            elif i<(red+white):
                nums[i]=1
            else:
                nums[i]=2

class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        zero=-1
        one=-1
        for i in range(0,len(nums)):
            if nums[i] <2:
                one+=1
                
            if nums[i]==0:
                zero+=1
                nums[zero],nums[i]=nums[i],nums[zero]
                    
            if nums[i]==1:
                nums[one],nums[i]=nums[i],nums[one]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) < 2:
            return
        
        # create array of size k initialized to 0s
        counter = [0] * 3
		# go through array to sort and increment counts for k
        for n in nums:
            counter[n] += 1

		# set index pointer to 0
        # set counter pointer to 0 (via for loop)
        numsIndex = 0
        for counterIndex in range(3):
		    # while we have elements left at this index, do work
            while counter[counterIndex] > 0:
                nums[numsIndex] = counterIndex
				# decrement elements remaining and increment our position in the original list
                counter[counterIndex] -= 1
                numsIndex += 1