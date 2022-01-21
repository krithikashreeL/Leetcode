class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix) 
        cols = len(matrix[0])
        for i in range (1,rows):
            for j in range (cols):
                if j == 0:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j+1])
                elif j == cols-1:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j-1])
                else:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j-1],matrix[i-1][j+1])
        return min(matrix[rows-1])