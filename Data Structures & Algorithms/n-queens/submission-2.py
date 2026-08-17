class Solution:

    def __init__(self):
        self.ans = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [
            ['.' for _ in range(n)] for _ in range(n)
        ]
        self.backtrack(board, 0, n)
        return self.ans

    def backtrack(self, board, row, n):

        # add result
        if row == n:
            self.ans.append([''.join(row) for row in board])
            return

        for col in range(n):
            if not self.isvalid(board, row, col, n):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row + 1, n)
            board[row][col] = '.'
    
    def isvalid(self, board, row, col, n):
        # check above
        r, c = 0, col
        while r < row:
            if board[r][c] == 'Q':
                return False
            r += 1

        # check left above
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        
        # check right above
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1
        return True