More notes:

https://www.notion.so/paulonteri/Recursion-DP-Backtracking-525dddcdd0874ed98372518724fc8753#fb64620280c74255982bb1d93455881b


class Solution:
    def numDecodings(self, s: str):
        return self.helper(s, 0, [None]*len(s))

    def helper(self, s, idx, cache):
        if idx == len(s):
            return 1
        if cache[idx] is not None:
            return cache[idx]

        ways = 0

        if s[idx] != "0":
            # length one
            ways += self.helper(s, idx+1, cache)

            # length two
            if idx < len(s)-1:
                num = int(s[idx:idx+2])

                if num >= 1 and num <= 26:
                    ways += self.helper(s, idx+2, cache)

        cache[idx] = ways
        return cache[idx]


""" 
Bottom up DP
"""


class SolutionBU:
    def numDecodings(self, s: str):
        """ 
        What if s was of length 1? 2? 3? 4? ... n?
        """
        if not s or s[0] == "0":
            return 0

        # # create array to store the subproblem results ---------------------------------
        dp = [0]*len(s)
        dp[0] = 1
        # index 1: should handle 10, 11, 33, 30
        if len(s) >= 2:
            # Check if successful single digit decode is possible.
            if s[1] != '0':
                dp[1] = 1
            # Check if successful two digit decode is possible.
            two_digit = int(s[:2])
            if two_digit >= 10 and two_digit <= 26:
                dp[1] += 1

        # # fill in subproblem results ----------------------------------------------------------
        for i in range(2, len(dp)):
            # Check if successful single digit decode is possible.
            if s[i] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i-1: i+1])
            if two_digit >= 10 and two_digit <= 26:
                # result: dp[i] = dp[i - 1] + dp[i - 2]
                dp[i] += dp[i - 2]

        return dp[-1]


class SolutionBU2:
    def numDecodings(self, s: str):
        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2: i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]


""" 
Iterative, Constant Space
"""


class SolutionITER:
    def numDecodings(self, s: str):
        if s[0] == "0":
            return 0

        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = one_back
            two_digit = int(s[i - 1: i + 1])
            if two_digit >= 10 and two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current

        return one_back


class Solution:
    def numDecodings(self, s: str) -> int:
            
        def decode(s,i=0,cache={}):
            if i in cache:
                return cache[i]
            if i == len(s):
                return 1
            if int(s[i]) == 0:
                return 0
            count = decode(s, i+1)
            if (i+1 < len(s)) and (int(s[i:i+2]) <= 26):
                count += decode(s, i+2)
            if i not in cache:
                cache[i] = count
            return cache[i]
            
        return decode(s)