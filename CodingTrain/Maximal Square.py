Introduction
We are given a m x n array matrix and we need to find the largest square such that all elements in this square is '1'.

Approach 1: Brute Force
Simple enough. For each coordinate (x, y) in matrix, we check if matrix[x][y] == '1'. If so, then we know that there exists a square at (x, y) that is at least 1 x 1 in size. We can then continue checking if a bigger square exists by looking at the adjacent coordinates of (x, y).

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr = 0  # current length of the square at (i, j)
                flag = True  # indicates if there still exists a valid square
                while flag:
                    for k in range(curr+1):
                        # check outer border of elements for '1's.
                        """
                        eg curr = 2, ie a valid 2x2 square exists
                        'O' is valid, check 'X':
                        X X X
                        X O O
                        X O O
                        """
                        if i < curr or j < curr or \
                                matrix[i-curr][j-k] == '0' or \
                                matrix[i-k][j-curr] == '0':
                            flag = False
                            break
                    curr += flag
                if curr > result:  # new maximum length of square obtained
                    result = curr
        return result*result  # area = length x length
TC: O(mnk^{2}), where k is the length of the maximal square, since the while loop will iterate from curr = 0 to curr = k+1.
SC: O(1), since no additional data structures were used.

Approach 2: Obtaining DP Approach
Obviously, the brute force way of checking for valid squares isn't very efficient. We need to think of another way to determine whether an n x n square is valid. For this, let's start with the simplest non-trivial case: a 2 x 2 square.

Recall from the brute force approach that the way we check for validity is by checking the outer border, i.e.:

e.g. curr = 1, i.e. a valid 1 x 1 square exists (matrix[x][y] == '1').
'O' is valid, check for 'X':
X X
X O
To check for 'X', we would need to check if matrix[x-1][y] == '1', matrix[x][y-1] == '1' and matrix[x-1][y-1] == '1'. Except, because of the way the outer for loops were written, note that we have checked each of these before! To reach matrix[x][y] would require us to loop over the previous indexes, which include all of (x-1, y-1), (x-1, y) and (x, y-1). If any of the previous indexes are '0', then the maximal square that exists at (x, y) can only be a 1 x 1 square.

Different possible combinations of maximal square sizes in a 2x2 matrix
comb   0 0   1 0   0 1   0 0   0 0   1 1   1 0   1 0   0 1   0 1   0 0   1 1   1 1   1 0   0 1   1 1
       0 0   0 0   0 0   1 0   0 1   0 0   1 0   0 1   1 0   0 1   1 1   1 0   0 1   1 1   1 1   1 1
no 1s  -0-   ----------1----------   ----------------2----------------   ----------3----------   -4-
size   -------------------------------------------1-------------------------------------------   -2-
Note the length of the maximal square for each possible combination. This can be simplified and generalised to the following equation:

Length of maximal square at:
matrix[x-1][y-1]: a   matrix[x-1][y]: b
 matrix[x][y-1]: c           '1'
Length of maximal square at matrix[x][y] (given matrix[x][y] == '1') is min(a, b, c) + 1

Example matrix:
0 0 1 1 1
0 0 1 1 1
0 1 1 1 1
0 1 1 1 1
Length of maximal sqaures at:
	matrix[2][3] = 2x2
	matrix[2][4] = 3x3
	matrix[3][3] = 2x2
	matrix[3][4] = min(2x2, 3x3, 2x2) + 1 = 2x2 + 1 = 3x3
Therefore, we can store the length of the maximal squares at these coordinates in a separate matrix and retrieve it later for O(1) computation.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        dp = [[0]*n for _ in range(m)]  # dp[x][y] is the length of the maximal square at (x, y)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':  # ensure this condition first
                    # perform computation, mind border restrictions
                    dp[i][j] = min(dp[i-1][j] if i > 0 else 0,
                                   dp[i][j-1] if j > 0 else 0,
                                   dp[i-1][j-1] if i > 0 and j > 0 else 0) + 1
                    if dp[i][j] > result:
                        result = dp[i][j]
        return result*result
TC: O(mn), since the computation for valid maximal square takes O(1) time.
SC: O(mn), due to the maintenance of the DP array.

Approach 3: Intuitive Optimised DP
If we take some time to analyse the formula used for the computation of the length of the maximal square at (x, y), we notice that we only ever use three different variables: dp[x-1][y-1], dp[x-1][y] and dp[x][y-1]. These variables only require 2 rows of DP arrays for storage: the previous row x - 1, and the current row x. As such, instead of using a m x n DP array, we can use a 2 x n DP array instead.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        prev, curr = [0]*n, [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    curr[j] = min(curr[j-1] if j > 0 else 0,
                                  prev[j-1] if j > 0 else 0,
                                  prev[j]) + 1
                    if curr[j] > result:
                        result = curr[j]
            prev, curr = curr, [0]*n
        return result*result
TC: O(mn), as discussed previously.
SC: O(mn), due to the creation of m arrays of length n.

The implementation above does not actually optimise for space, but we can do so by setting curr = prev. Since the values in prev will not be used, we can simply override them.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        prev, curr = [0]*n, [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    curr[j] = min(curr[j-1] if j > 0 else 0,
                                  prev[j-1] if j > 0 else 0,
                                  prev[j]) + 1
                else:
                    curr[j] = 0  # reset curr[j]
                if curr[j] > result:
                    result = curr[j]
            prev, curr = curr, prev
        return result*result
TC: O(mn), as discussed previously.
SC: O(2n) \approx O(n). We only create 2 arrays of length n and alternate between them.

We can also write it in the following manner:

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        dp = [[0]*n for _ in range(2)]  # 2-rowed dp array
        for i in range(m):
            for j in range(n):
                # i%2 (or i&1) alternates between dp[0] and dp[1]
                dp[i%2][j] = 0 if matrix[i][j] == '0' else \
                    (min(dp[i%2][j-1] if j > 0 else 0,
                        dp[1-i%2][j-1] if j > 0 else 0,
                        dp[1-i%2][j]) + 1)
                result = dp[i%2][j] if dp[i%2][j] > result else result
        return result*result
TC: O(mn), as discussed previously.
SC: O(2n) \approx O(n), as discussed previously.

Approach 4: Optimised DP
Finally, we can get rid of the need for 2D arrays. By applying the same computation on the same array, we can assert that the current value dp[j] points to the previous result dp[i-1][j]. dp[j-1] maps to dp[i][j-1], since this value would have already been computed and replaced before we iterated to index j.

The only value which we do not have is dp[i-1][j-1], which cannot simply be obtained from the array. As such, we will use another variable to store dp[i-1][j-1]] specifically for computation purposes.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n, result = len(matrix), len(matrix[0]), 0
        dp = [0]*n  # 1D array
        for i in range(m):
            prev = 0  # stores dp[i-1][j-1]
            for j in range(n):
                dp[j], prev = 0 if matrix[i][j] == '0' else \
                    (min(dp[j],  # dp[j] -> dp[i-1][j]
                         dp[j-1] if j > 0 else 0,  # dp[j-1] -> dp[i][j-1]
                         prev)  # prev -> dp[i-1][j-1]
                    + 1), dp[j]
                result = dp[j] if dp[j] > result else result
        return result*result