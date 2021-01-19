#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for n, i, j in trips:
            heapq.heappush(heap, (j, -n))
            heapq.heappush(heap, (i, n))
        while heap:
            capacity -= heapq.heappop(heap)[1]
            if capacity < 0:
                return False
        return True
# @lc code=end
