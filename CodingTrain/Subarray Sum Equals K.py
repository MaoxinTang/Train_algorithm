class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
    
    
    # Running sum approach
        currsum = 0
        subarray = 0
        hashmap = {}
    
    # looping through each and every number in the nums array
        for num in nums:
            currsum += num # Adding the number to the current sum
        
            if currsum == k: # If current sum is found to be equal to k then we directly increment the subarray
                subarray += 1

            if currsum - k in hashmap: # If currentsum - k is found in hashmap then we increment the subarray to the value of current sum - k in hashmap
                subarray += hashmap[currsum - k]

            if currsum in hashmap: # if current sum is already in hashmap then we increment the value of that particular current sum in hashmap to 1
                hashmap[currsum] += 1

            else: # If the current sum is not in hashmap then we se tthe value of currentsum to 1 in hashmap
                hashmap[currsum] = 1
        
        return subarray # Return the subarray count in the end