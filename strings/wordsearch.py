class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    res = self.recur(board, word, i, j)
                    if res: return True
        return False
    
    def recur(self, board, word, i, j):
        if len(word) <= 0: return True
        if i > self.m-1 or j > self.n-1 or i < 0 or j <0: return False
        if board[i][j] == word[0]:
            board[i][j] = -1
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                res = self.recur(board, word[1:], i+x, j+y)
                if res: return True
            board[i][j] = word[0]

        return False
        