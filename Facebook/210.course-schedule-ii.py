#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        ans = []

        for x, y in prerequisites:
            graph[y].append(x)

        def dfs(i,graph, visit, ans):
            if visit[i] == -1:
                return True
            if visit[i] == 1:
                return False
            visit[i] = -1
            for j in graph[i]:
                if dfs(j, graph, visit, ans):
                    return True
            visit[i] = 1
            ans.append(i)
            return False
        for i in range(numCourses):
            if dfs(i, graph, visit, ans):
                return []
        return ans[::-1]

# @lc code=end
