class Solution:
    def findOrder(self, numCourses, prerequisites):
        outdegree = collections.defaultdict()
        indegree = [0 for _ in range(numCourses)]
        res = []

        for succ, pre in prerequisites:
            outdegree[succ].append(pre)
            indegree[succ] += 1

        q = collections.deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                res.append(i)
        count = 0
        while q:
            cur = q.popleft()
            count += 1
            for nb in outdegree[cur]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)
                    res.append(nb)
        return res if count == numCourses else []
