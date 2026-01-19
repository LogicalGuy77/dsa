from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    if self.explore(i, j, board, word, 0):
                        return True
                    
        return False

    def explore(self, i , j, board, word, start):
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or start>=len(word) or board[i][j]!=word[start]:
            return False
        if start == len(word)-1:
            return True

        temp = board[i][j]
        board[i][j] = '#'

        ans = (self.explore(i-1, j, board, word, start+1) or
            self.explore(i, j-1, board, word, start+1) or
            self.explore(i, j+1, board, word, start+1) or
            self.explore(i+1, j, board, word, start+1))
        
        board[i][j] = temp
        return ans

obj = Solution()
print(obj.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))