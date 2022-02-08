# DP (top-down) solution
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        t = [[0 for p in range(0,m+1)]
            for q in range(0,n+1)]
        
        for a in range(0,n+1):
            t[a][0] = a
        for b in range(1,m+1):
            t[0][b] = b
            
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if word1[i-1] == word2[j-1]:
                    t[i][j] = t[i-1][j-1]
                    
                else:
                    t[i][j] = 1 + min(t[i][j-1], t[i-1][j], t[i-1][j-1])
                    
        return t[n][m]
		
		
# Recursive code
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.edit(word1,word2,len(word1), len(word2))
    
    def edit(self,x,y,n,m):
        if n == 0 or m == 0:
            if n == 0:
                return m
            else:
                return n
            
        if x[n-1] == y[m-1]:
            return self.edit(x,y,n-1,m-1)
        else:
            return 1 + min(self.edit(x,y,n,m-1), self.edit(x,y,n-1,m), self.edit(x,y,n-1,m-1))