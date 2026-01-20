from typing import List

class Solution:
    def findPath(self, m: List[List[int]], n: int) -> List[str]:
        # Your code here
        # Return the list of all possible paths in lexicographical order DLRU
        res = []
        path = ''

        def recur(grid, path, n, i, j):
            
            if i< 0 or i>=n or j<0 or j>=n or grid[i][j] != 1:
                return
            if i == n-1 and j==n-1:
                res.append(path)
                return
            
            visited = grid[i][j]
            grid[i][j] = -1

            # Down
            recur(grid, path+'D', n, i+1, j)
            # Left
            recur(grid, path+'L', n, i, j-1)
            # Right
            recur(grid, path+'R', n, i, j+1)
            # Up
            recur(grid, path+'U', n, i-1, j)

            grid[i][j] = visited

        recur(m, path, n, 0, 0)
        return res

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n1 = 4
    grid1 = [
        [1, 0, 0, 0], 
        [1, 1, 0, 1], 
        [1, 1, 0, 0], 
        [0, 1, 1, 1]
    ]
    print("Example 1:")
    result1 = sol.findPath(grid1, n1)
    if not result1:
        print(-1)
    else:
        print(" ".join(result1))
        
    print("-" * 20)

    # Example 2
    n2 = 2
    grid2 = [
        [1, 0], 
        [1, 0]
    ]
    print("Example 2:")
    result2 = sol.findPath(grid2, n2)
    if not result2:
        print(-1)
    else:
        print(" ".join(result2))
