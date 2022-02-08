NOTE: The below solution will give TLE, idk why, so rather use for loop instead of while loop, can't see what am doing wrong, look at solution 1 and solution 2.

class Solution:
    
    # Recursion  with memoization
    def numSquares(self, n: int) -> int:
        
        leastSqrs = n
        
        @cache
        def recursion(s):
            nonlocal leastSqrs
            if s > 3:
                i = 1
                while i**2 <= s:
                    leastSqrs = min(leastSqrs, 1 + recursion(s-i**2))
                    i += 1
                return leastSqrs
            return s
        
        return recursion(n) 
Solution 1

from collections import defaultdict

class Solution:
    
    # Recursion  with memoization
    def numSquares(self, n: int) -> int:
        
        # Init
        sqrs = []
        i = 1
        while i**2 <= n:
            sqrs.append(i**2)
            i += 1
        
        leastSqrs = n
        
        @cache
        def recursion(s):
            nonlocal leastSqrs
            if s > 3:
                for sqr in sqrs:
                    if sqr <= s:
                        leastSqrs = min(leastSqrs, 1 + recursion(s-sqr))
                    else:
                        break
                return leastSqrs
            return s
        
        return recursion(n) 
Solution 2

from collections import defaultdict

class Solution:
    
    # Unbounded knapsack approach (DP)
    def numSquares(self, n: int) -> int:
        
        # Init
        sqrs = []
        i = 1
        while i**2 <= n:
            sqrs.append(i**2)
            i += 1
            
        dp = defaultdict(lambda: n)
        for i in range(4):
            dp[i] = i
        
        for i in range(3,n+1):
            for sqr in sqrs:
                if sqr <= i:
                    dp[i] = min(dp[i], 1 + dp[i-sqr])
                else:
                    break
                    
        return dp[n]