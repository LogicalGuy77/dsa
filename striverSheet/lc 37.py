# from typing import List

# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         def solve():
#             for i in range(9):
#                 for j in range(9):
#                     if board[i][j] == '.':
#                         for k in map(str, range(1, 10)):
#                             if self.isValid(board, i, j, k):
#                                 board[i][j] = k
#                                 if solve() == True:
#                                     return True
#                                 else:
#                                     board[i][j] = '.'
#                         return False
#             return True
            
#         solve()
    
#     def isValid(self, board, i, j , k):
#         for itr in range(0, 9):
#             if board[itr][j] == k:
#                 return False
#             if board[i][itr] == k:
#                 return False
#             if board[3*(i//3)+ itr//3][3*(j//3) + itr%3] == k:
#                 return False
#         return True
                              
                                        



# obj = Solution()
# board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
# obj.solveSudoku(board)

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empties.append((i, j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3)*3 + j//3].add(board[i][j])

        def solve(idx=0):
            if idx == len(empties):
                return True
            i, j = empties[idx]
            b = (i//3)*3 + j//3
            for k in "123456789":
                if k not in rows[i] and k not in cols[j] and k not in boxes[b]:
                    board[i][j] = k
                    rows[i].add(k)
                    cols[j].add(k)
                    boxes[b].add(k)
                    if solve(idx+1):
                        return True
                    board[i][j] = '.'
                    rows[i].remove(k)
                    cols[j].remove(k)
                    boxes[b].remove(k)
            return False

        solve()

obj = Solution()
board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
obj.solveSudoku(board)
print(board)