# @lc app=leetcode id=210 lang=python3
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        res = []

        for cur, pre in prerequisites:
            adj_list[pre].append(cur)
            indegree[cur] += 1

        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                res.append(i)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                    res.append(nei)
        return res if count == numCourses else []
