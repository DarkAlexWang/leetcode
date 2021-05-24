# @lc lang=python3
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {}
        for e in employees:
            dic[e.id] = e

        q = collections.deque()
        q.append(id)
        res = 0
        while q:
            s = q.popleft()
            if s not in dic:
                return 'error'

            res += dic[s].importance
            for p in dic[s].subordinates:
                q.append(p)
        return res
