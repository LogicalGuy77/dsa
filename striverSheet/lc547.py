class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(node, visited, isConnected):
            visited[node] = 1
            for j in range(0, len(isConnected)):
                if visited[j] != 1 and isConnected[node][j]==1:
                    dfs(j, visited, isConnected)
            return
              



        visited = [0]*len(isConnected)
        count = 0
        for i in range(0, len(isConnected)):
            if visited[i]!=1:
                count+=1
                dfs(i, visited, isConnected)
        
        return count


isConnected = [[1,0,0],[0,1,0],[0,0,1]]
obj = Solution()
obj.findCircleNum(isConnected)