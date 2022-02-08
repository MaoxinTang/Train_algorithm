Solution 1 (DP)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        lookup = [[m+n for _ in range(n)] for _ in range(m)]
		"""
			Since it is very hard to get to the base condition mat[row][col] == 0 every time so, lets go with worst scenario for every cell.
			1. Assign m+n to be the length for each cell to reach to the nearest zero.
			2. Traverse the matrix two times from top/left to bottom/right so that in the first traversal, previous rows/columns can be taken as base condition and in second traversal next rows/columns can be taken as base condition.
			In the first traversal, Start from the first cell and check for the nearest zero either in upward of backward direction.
			In the second traversal, Start from the last cell and check for the nearest zero either in downward of forward direction.
		"""
        # Either moving up or left
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    lookup[row][col] = 0
                else:
                    if row > 0:
                        lookup[row][col] = min(lookup[row][col], 1 + lookup[row - 1][col])
                    if col > 0:
                        lookup[row][col] = min(lookup[row][col], 1 + lookup[row][col - 1])
        # Either moving down or right
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row < m - 1:
                    lookup[row][col] = min(lookup[row][col], 1 + lookup[row + 1][col])
                if col < n - 1:
                    lookup[row][col] = min(lookup[row][col], 1 + lookup[row][col + 1])
        return lookup
Solution 2 (BFS)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        """
            Since we don't have a straight forward base case to find the nearest zero for any cell, so to solve this type of questions, reverse engineering is required.
            The idea is to first keep a track of all the cells having zero in a queue and then use BFS to update the value of nearest zero for its neighbours.
            Since BFS is used, so once a value for any element is found, the values for its neighbours would also be found.
        """

        visited = [[None for _ in range(n)] for _ in range(m)]        
        queue = []
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row,col))
                    visited[row][col] = True
        
        
        while queue:
            row, col = queue.pop(0)
            for r, c in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
                if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                    visited[r][c] = True
                    mat[r][c] = 1 + mat[row][col]
                    queue.append((r, c))
        return mat