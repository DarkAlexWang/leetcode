#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = []
        for _ in range(N + 1):
            self.graph.append([])
        for a, b in dislikes:
            self.graph[a].append(b)
            self.graph[b].append(a)
        self.colors = [0] * (N + 1)

        for i in range(N):
            if self.colors[i] == 0 and not self.dfs(i, 1):
                return False
        return True

    def dfs(self,cur, color):
        self.colors[cur] = color
        for nxt in self.graph[cur]:
            if self.colors[nxt] == color:
                return False
            if self.colors[nxt] == 0 and not self.dfs(nxt, -color):
                return False
        return True
# @lc code=end
