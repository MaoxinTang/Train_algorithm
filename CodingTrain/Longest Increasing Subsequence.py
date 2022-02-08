Implementation by Solitaire order with O( n lg n ):

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        Rightmost = -1
        poker_slot = []
        
        for number in nums:
            
            if not poker_slot or poker_slot[Rightmost] < number:
                poker_slot.append( number)
            
            else:
                inser_index = bisect.bisect_left(poker_slot, number)
                poker_slot[ inser_index ] = number
        
        return len(poker_slot)
or

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        slots = [0 for _ in range(n)]
        
        valid_slot = 0
        
        for number in nums:
            
            # put number in solitarie order
            left, right = 0, valid_slot
            
            # binary search to find leftmost feasible slot index
            while left < right:
                
                mid = (left + right)//2
                
                if number > slots[mid]:
                    left = mid+1
                
                else:
                    right = mid
            
            # put current number to leftmost feasible slot
            put_index = left
            slots[put_index] = number
            valid_slot = max(put_index+1, valid_slot)
        
        return valid_slot
Share another implementation with bottom-up 2D DP with O(n^2)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:    
        
        size = len(nums)
        
        # default value is 1, because each array element itself can be smallest LIS with length = 1
        len_LIS = [1 for _ in range(size)]
        
        # for each subsequence ending at index i
        for i in range(size):
            
            # for each prefix subsequence ending at k
            for k in range(i):
            
                if nums[k] < nums[i]:
                    
                    # check if we can extend LIS length from prefix subsequence
                    len_LIS[i] = max(len_LIS[i], len_LIS[k]+1)
                    
        
        return max(len_LIS)
Share another implementation with top-down 2D DP with O(n^2)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:    
        
        # Use python native cache as memoization for DP
        @cache
        def dp( i ):
            # input: index i of array
            # output: solve LCS with array ending at index i
            
            if i == 0:
                ## Base case
                # nums[0] itself is the smallest increasing subsequence
                return 1
            
            ## General cases
            prev_LIS = [ dp(k) for k in range(i) ]
            cur_LIS = max( prev_LIS[k]+1 if (nums[k] < nums[i]) else 1 for k in range(i) )
            
            # update global LIS length
            dp.global_LIS_length = max(dp.global_LIS_length, cur_LIS)
            
            return cur_LIS

        # ----------------------

        
        # smallest LIS length is 1, because each array number itself can be the smallest LIS
        dp.global_LIS_length = 1
        
        dp( len(nums)-1 )

        return dp.global_LIS_length