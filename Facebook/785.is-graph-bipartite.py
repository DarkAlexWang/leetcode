#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n, colored = len(graph), {}
        for i in range(n):
            if i not in colored and graph[i]:
                colored[i] = 1
                q = collections.deque([i])
                while q:
                    cur = q.popleft()
                    for nb in graph[cur]:
                        if nb not in colored:
                            colored[nb] = -colored[cur]
                            q.append(graph[nb])
                        elif colored[nb] == colored[cur]:
                            return False
        return True

# @lc code=end
