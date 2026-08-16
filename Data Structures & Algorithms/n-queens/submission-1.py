class Solution:
    def __init__(self):
        self.ans = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [
            ['.' for _ in range(n)]
            for _ in range(n)
        ]
        self.backtrack(board, 0)
        return self.ans
        
    def backtrack(self, board, row):

        def is_valid(board, row, col):
            # check above
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q': return False
                i -= 1; j -= 1
            i, j = row - 1, col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q': return False
                i -= 1; j += 1
            return True

        # cur row > board last row, means board filled
        n = len(board)
        if row == n:
            self.ans.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if not is_valid(board, row, col):
                continue
            
            board[row][col] = 'Q'
            self.backtrack(board, row + 1)
            board[row][col] = '.'
