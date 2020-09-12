#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        for i, node in enumerate(graph):
            if not self.bfs(node, visited):
                return False
        return True

    def bfs(self, node, visited):
        #if node in visited:
        #    return True
        print(visited)
        q = deque([node])
        visited[node] = 0
        while q:
            cur = q.popleft()
            curgroup = visited.get(cur)
            neigroup = 1 if curgroup == 0 else 0
            for nei in enumerate(cur):
                if nei not in visited:
                    visited[nei] = neigroup
                    q.pushleft(nei)
                elif visited[nei] != neigroup:
                    return False
        return True
#        n, colored = len(graph), {}
#        for i in range(n):
#            if i not in colored and graph[i]:
#                colored[i] = 1
#                q = collections.deque([i])
#                while q:
#                    cur = q.popleft()
#                    for nb in graph[cur]:
#                        if nb not in colored:
#                            colored[nb] = -colored[cur]
#                            q.append(nb)
#                        elif colored[nb] == colored[cur]:
#                            return False
#        return True
# @lc code=end
