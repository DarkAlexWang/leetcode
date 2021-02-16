#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree = [0] * len(graph)
        indegree = [[] for _ in range(len(graph))]

        for i in range(len(graph)):
            outdegree[i] = len(graph[i])
            for j in range(len(graph[i])):
                indegree[graph[i][j]].append(i)
        q = collections.deque()
        for i in range(len(outdegree)):
            if outdegree[i] == 0:
                q.append(i)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            if indegree[node]:
                for rest in indegree[node]:
                    outdegree[rest] -= 1
                    if outdegree[rest] == 0:
                        q.append(rest)
        return sorted(res)

# @lc code=end
