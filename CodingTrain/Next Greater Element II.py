class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Its like maintain a monotonic increasing stack with [index,val]
        # if current val greater than stack[-1], then index, val = stack.pop() and assign to res[index] = val
        # n = len(nums) at must find within n + n-1 times
        # Time: O(n) , Space O(n)
        

        n = len(nums)
        res = [-1] * n
        stack = []    # mono_increase_stack
        
        at_most_times = n+(n-1)
        for i in range(at_most_times):
            index = i%n
            while stack and stack[-1][1] < nums[index]:
                res_index,_ =stack.pop()
                res[res_index] = nums[index]
            stack.append([index,nums[index]])
            
        return res