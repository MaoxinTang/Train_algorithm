class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        
        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]


        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]