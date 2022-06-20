class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            for j in range(int(n/2)):
                swap = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = swap
        
        for i in range(n-1):
            for j in range(n-i-1):
                swap = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = swap
