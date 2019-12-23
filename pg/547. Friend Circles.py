# dfs recursive
class Solution:
    def findCircleNum(self, M):
        result = 0
        visited = [0] * len(M)
        for i in range(len(M)):
            if visited[i] == 0:
                self.dfs(M, visited, i)
                result += 1
        return result
    
    def dfs(self, M, visited, i):
        for j in range(len(M)):
            if visited[j] == 0 and M[i][j] == 1:
                visited[j] = 1
                self.dfs(M, visited, j)

# dfs iterative
class Solution3:
    def findCircleNum(self, M):
        result = 0
        visited = [0] * len(M)
        stack = []
        for i in range(len(M)):
            if visited[i] == 0:
                stack.append(i)
                while stack:
                    out = stack.pop()
                    visited[out] = 1
                    for j in range(len(M)):
                        if visited[j] == 0 and M[out][j] == 1:
                            stack.append(j)
                result += 1
        return result

# bfs
from collections import deque
class Solution2:
    def findCircleNum(self, M):
        result = 0
        visited = [0] * len(M)
        q = deque([])
        
        for i in range(len(M)):
            if visited[i] == 0:
                q.append(i)
                while q:
                    out = q.popleft()
                    visited[out] = 1
                    for j in range(len(M)):
                        if visited[j] == 0 and M[out][j] == 1:
                            q.append(j)
                result += 1
        return result
                            