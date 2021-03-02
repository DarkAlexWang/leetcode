#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#

# @lc code=start
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        islands = Union()
        for p in map(tuple, positions):
            islands.add(p)
            for dp in (0,1), (0, -1), (1, 0), (-1, 0):
                q = (p[0] + dp[0], p[1] + dp[1])
                if q in islands.group:
                    islands.union(p, q)
            ans += [islands.count]
        return ans

class Union(object):
    def __init__(self):
        self.group = {}
        self.island = {}
        self.count = 0

    def add(self, p):
        self.group[p] = p
        self.island[p] = 1
        self.count += 1

    def find(self, i):
        if i == self.group[i]:
            return i
        else:
            return self.find(self.group[i])

    def union(self, p, q):
        root1, root2 = self.find(p), self.find(q)
        if root1 == root2:
            return
        if self.island[root1] > self.island[root2]:
            root1, root2 = root2, root1
        self.group[root1] = root2
        self.island[root2] += self.island[root1]
        self.count -= 1

# @lc code=end
