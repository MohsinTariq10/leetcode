class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1], [1,1]]
        if numRows == 1:
            return [pascal[0]]
        elif numRows == 2:
            return pascal
        for i in range(1, numRows-1):
            row = [1]
            for j in range(len(pascal[i-1])):
                row.append(pascal[i][j] + pascal[i][j+1])
            row.append(1)
            pascal.append(row)
            print(pascal)
        return pascal
            