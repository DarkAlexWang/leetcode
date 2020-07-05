#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        # states: 0 = unknown, -1 == visiting, 1 = visited
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


## Topological sorting:

# for each notde:
#   if not marked:
#       if (dfs(node) == CYCLE) return CYCLE
# return OK
#
# dfs(node):
#   if node is marked as visited: return OK
#   if node is marked as visiting: return CYCLE
#   mark node as visiting
#   for each new_node in node.neighbors:
#       if dfs(new_node) == CYCLE: return CYCLE
#   mark node as visited
#  #add node to the head of ordered_list
#   return OK

# @lc code=end
