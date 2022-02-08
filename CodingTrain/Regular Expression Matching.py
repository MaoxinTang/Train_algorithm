import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return not re.match(f"^{p}$", s) is None

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.fullmatch(p, s)!=None
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @functools.lru_cache(None)
        def foo(i, j):
            if i==j==-1:
                return True

            if j<0:
                return False
            
            if i<0:
                return p[j]=="*" and foo(i, j-2)
                
            if p[j]=="*":
                if foo(i, j-2): 
                    return True
                
                if (p[j-1]=="." or s[i]==p[j-1]) and foo(i-1, j):   
                    return True
                        
            elif (p[j]=="." or p[j]==s[i]) and foo(i-1, j-1):
                return True

            return False
                
        return foo(len(s)-1, len(p)-1)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = [[0]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = 1
        
        for i,el in enumerate(p, 1):
            if el=="*":
                dp[0][i] = dp[0][i-2]
        
        for i in range(len(s)):
            for j in range(len(p)):
                x = i+1
                y = j+1
                if s[i]==p[j] or p[j]=='.':
                    dp[x][y] = dp[x-1][y-1]
                
                elif p[j]=="*":
                    dp[x][y] = dp[x][y-2]
                    
                    if p[j-1]=="." or p[j-1]==s[i]:
                        dp[x][y] = dp[x-1][y] or dp[x][y]
                        
        return dp[-1][-1]