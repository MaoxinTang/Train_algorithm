class Solution:
    def countSubstrings(self, s: str) -> int:
        def build_palindrome1(i):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.ret += 1
                l -= 1
                r += 1
        def build_palindrome2(i, j):
            l, r = i, j
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.ret += 1
                l -= 1
                r += 1
                
        self.ret = 0
        for i in range(len(s)):
            build_palindrome1(i)
            if i < len(s)-1:
                build_palindrome2(i, i+1)
        return self.ret