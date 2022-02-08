from itertools import count, takewhile
class Solution:
    def longestConsecutive(self, nums):
        return reduce(max, (lambda s: (sum(len(list(takewhile(lambda x: x in s and (s.remove(x) or 1), count(n+i[0],i[1])))) 
															for i in [(0,-1),(1,1)]) for n in nums if n in s))(set(nums)), 0)
