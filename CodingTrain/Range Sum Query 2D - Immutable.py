class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix) + 1, len(matrix[0]) + 1
        self.dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                self.dp[i][j] = self.dp[i - 1][j] + self.dp[i][j - 1] + matrix[i - 1][j - 1] - self.dp[i - 1][j - 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.dp[row2][col2] - self.dp[row1 - 1][col2] - self.dp[row2][col1 -1] + self.dp[row1 - 1][col1 - 1]