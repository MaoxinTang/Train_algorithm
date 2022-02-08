class Solution:
	def minPathSum(self, grid: List[List[int]]) -> int:
		n = len(grid)
		m = len(grid[0])
		array = [[0]*m for i in range(n)]

		array[0][0] = grid[0][0]
		for j in range(1, m):#fill in the first line
			array[0][j] = array[0][j-1] + grid[0][j]

		for i in range(1, n):#fill in the first column
			array[i][0] = array[i-1][0] + grid[i][0]
		#fill in our array, where the value of each cell corresponds to the shortest path to it
		for i in range(1, n):
			for j in range(1, m):
				array[i][j] = min(array[i][j-1], array[i-1][j]) + grid[i][j]

		return array[n-1][m-1]
