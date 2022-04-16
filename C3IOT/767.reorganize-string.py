#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        res, C = [], Counter(s)
        heap = [(-value, key) for key, value in C.items()]
        heapq.heapify(heap)
        prev_a, prev_b = 0, ''

        while heap:
            a, b = heapq.heappop(heap)
            res += [b]
            if prev_a < 0:
                heapq.heappush(heap, (prev_a, prev_b))
            a += 1
            prev_a, prev_b = a, b
        res = ''.join(res)
        if len(res) != len(s):
            return ''
        return res
# @lc code=end
