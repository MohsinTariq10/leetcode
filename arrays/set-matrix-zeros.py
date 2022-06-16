class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cols[j] = 1
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i] = [0] * n
                if cols[j] == 1:
                    matrix[i][j] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and matrix[i][j] != 'c' and matrix[i][j] != 'r':
                    for x in range(m): 
                        if matrix[x][j]!=0: matrix[x][j] = 'c'
                    for x in range(n):
                        if matrix[i][x]!=0: matrix[i][x] = 'r'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'c' or matrix[i][j] == 'r':
                    matrix[i][j] = 0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row = False
        first_col = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True
                    if j == 0:
                        first_col = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            if (matrix[i][0] == 0):
                matrix[i][1:] = [0]*(n-1)
        for j in range(1, n):
            if (matrix[0][j] == 0):
                for x in range(1, m):
                    matrix[x][j] = 0
        if first_row:
            matrix[0] = [0]*n
        if first_col:
            for x in range(m):
                matrix[x][0] = 0
