class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        temp = []
        out = []
        for i in range(len(nums)):
            while len(temp)>0:
                if temp[-1] < nums[i]:
                    temp.pop(-1)
                else:
                    break
            temp.append(nums[i])
            if i >= k-1:
                out.append(temp[0])
                if temp[0] == nums[i-k+1]:
                    temp.pop(0)
        return out