class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #using hash map
        #iterate through array
        #compare if element exists, if no, add to the has map, else return
        
        d={}
        for i in nums:
            if i in d:
                return i
            else:
                d[i]=True