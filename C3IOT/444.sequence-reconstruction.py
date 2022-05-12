#
# @lc app=leetcode id=444 lang=python3
#
# [444] Sequence Reconstruction
#

# @lc code=start
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        values = {x for seq in sequences for x in seq}
        graph = {x: [] for x in values}
        indegree = {x: 0 for x in values}

        for seq in sequences:
            for i in range(len(seq) - 1):
                s = seq[i] # source
                t = seq[i + 1] # target
                graph[s].append(t)
                indegree[t] += 1
        q = collections.deque()
        for node, count in indegree.items():
            if count == 0:
                q.append(node)
        res = []

        while q:
            if len(q) != 1:
                return False
            source = q.popleft()
            res.append(source)
            for target in graph[source]:
                indegree[target] -= 1
                if indegree[target] == 0:
                    q.append(target)
        return len(res) == len(values) and res == nums
# @lc code=end
