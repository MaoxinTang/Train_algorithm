class Solution:
    def longestPalindrome(self, s):
        C   = Counter(s)
        return (sum( (v>>1) for v in C.values() )<<1) + any( v%2 for v in C.values() )