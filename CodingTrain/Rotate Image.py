class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(1, len(matrix)):       
            for q in range(1,i+1):
                temp = matrix[i-q][i]
                matrix[i-q][i] = matrix[i][i-q]
                matrix[i][i-q] = temp
        
        for row in matrix:
            row.reverse()