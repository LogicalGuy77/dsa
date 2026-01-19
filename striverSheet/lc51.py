from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        ans = []


        def solve(col, board, n):
            if col>=n:
                ans.append(["".join(row) for row in board])
                return
            
            for row in range(0, n):
                if self.isSafe(row, col, board, n):
                    board[row][col] = 'Q'
                    solve(col+1, board, n)
                    board[row][col] = '.'



        solve(0, board, n)
        return ans

    def isSafe(self, row, col, board, n):

        cRow = row
        cCol = col

        while cRow>0 and cCol>0:
            cRow -= 1
            cCol -= 1
            if board[cRow][cCol] == 'Q':
                return False
        
        cRow = row
        cCol = col

        while cCol>0:
            cCol -= 1
            if board[cRow][cCol] == 'Q':
                return False
            
        cRow = row
        cCol = col

        while cRow<n-1 and cCol>0:
            cRow += 1
            cCol -= 1
            if board[cRow][cCol] == 'Q':
                return False
            
        return True


obj = Solution()
print(obj.solveNQueens(4))