Approach 1:- Recursion
TC:- Exponential (2^n)

class Solution:
    def climbStairs(self, n: int) -> int:
        def stairs(i):
            if i==0:
                return 1
            if i<0:
                return 0
        
            wayone=stairs(i-1)
            waytwo=stairs(i-2)
            
            return wayone+waytwo
        
    
        return stairs(n)
Approach 2:- Recursion+Memoization(Top Down DP)
TC:- O(N) but space complexity will still have stack space involved along with O(N) Dp array.


class Solution:
    def climbStairs(self, n: int) -> int:
        def stairs(i,dp):
            if i==0:
                return 1
            if i<0:
                return 0
            
            if dp[i]!=-1:
                return dp[i]
        
            wayone=stairs(i-1,dp)
            waytwo=stairs(i-2,dp)
            
            dp[i]= wayone+waytwo
            
            return dp[i]
        
        dp=[-1]*(n+1)
        return stairs(n,dp)
Approach 3:- Bottom Up DP
TC:- O(N) with no stack space involved but with a O(n) dp array.

class Solution:
    def climbStairs(self, n: int) -> int:
        def stairs(n,dp):
            for i in range(2,n+1):
                dp[i]=dp[i-1]+dp[i-2]
                
            return dp[n]
            
        dp=[-1]*(n+1)
        dp[0]=1
        dp[1]=1
        return stairs(n,dp)
Approach 4:- Space Optimisation technique!!!
TC:- O(N) with NO EXTRA SPACE!!!

class Solution:
    def climbStairs(self, n: int) -> int:
        def stairs(n):
            if n==0 or n==1:
                return 1
                
            a=1
            b=1
            for i in range(2,n+1):
                c=a+b
                a=b
                b=c
                
            return c
           
            
         return stairs(n)