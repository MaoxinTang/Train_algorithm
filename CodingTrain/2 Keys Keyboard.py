class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0]*(n+1)
        if(n==1): return 0
        dp[1] = 0
        if(n==2): return 2
        dp[2] = 2
        for i in range(3,n+1):
            max_fact = 1 if(i%2!=0) else 2
            if(max_fact!=2):
                for j in range(3,n//2,2):
                    if(i%j==0):
                        max_fact = j
                        break
            dp[i] = dp[i//max_fact]+max_fact if max_fact!=1 else i
        return dp[n]