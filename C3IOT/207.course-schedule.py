#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        outdegree = collections.defaultdict(list)
        indegree = [0 for _ in range(numCourses)]

        for succ, pre in prerequisites:
            outdegree[pre].append(succ)
            indegree[succ] += 1

        q = collections.deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        count = 0
        while q:
            cur = q.popleft()
            count += 1
            for nb in outdegree[cur]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)

        return count == numCourses

# @lc code=end
