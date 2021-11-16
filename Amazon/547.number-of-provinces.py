#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0 for _ in range(len(isConnected))]
        count = 0
        q = collections.deque()
        for i in range(len(isConnected)):
            if visited[i] == 0:
                q.append(i)
                while q:
                    cur = q.popleft()
                    visited[cur] = 1
                    for j in range(len(isConnected)):
                        if isConnected[cur][j] == 1 and visited[j] == 0:
                            q.append(j)
                count += 1
        return count
# @lc code=end
