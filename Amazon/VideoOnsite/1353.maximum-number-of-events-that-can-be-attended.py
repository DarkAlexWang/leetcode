#
# @lc app=leetcode id=1353 lang=python3
#
# [1353] Maximum Number of Events That Can Be Attended
#

# @lc code=start
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])
        total_days = max(end for start, end in events)
        day = 0
        event_id = 0
        num_events_attended = 0
        min_heap = []

        for day in range(1, total_days + 1):
            while event_id < len(events) and events[event_id][0] == day:
                heapq.heappush(min_heap, events[event_id][1])
                event_id += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                num_events_attended += 1
        return num_events_attended
# @lc code=end
