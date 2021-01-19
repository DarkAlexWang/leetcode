#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        heap = []
        answer = [0] * n
        for i, j, num in bookings:
            heapq.heappush(heap, (i - 1, num))
            heapq.heappush(heap, (j, -num))
        curr_num = 0
        prev_i = 0
        while heap:
            i, num = heapq.heappop(heap)
            for j in range(prev_i, i):
                answer[j] += curr_num
            prev_i = i
            curr_num += num
        return answer

# @lc code=end
