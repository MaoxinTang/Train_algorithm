class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        maximum=0
        for i in s:
            if i in seen:
                maximum = max(maximum,len(seen))
                seen = seen[seen.index(i)+1:] #slice 'seen' after the repeated element
            seen.append(i)
        maximum = max(maximum,len(seen))
        return maximum