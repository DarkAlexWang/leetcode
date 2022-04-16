#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        trips = sorted(trips, key = lambda x : (x[1], x[2]))
        curr = 0
        heap = []
        for i in range(n):
            while heap and heap[0][0] <= trips[i][1]:
                curr -= heap[0][1]
                heapq.heappop(heap)

            heapq.heappush(heap, (trips[i][2], trips[i][0]))
            curr += trips[i][0]

            if curr > capacity:
                return False
        return True
# @lc code=end
