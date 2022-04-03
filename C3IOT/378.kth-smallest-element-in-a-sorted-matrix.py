#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        minHeap = []
        for r in range(min(k, n)):
            minHeap.append((matrix[r][0], r, 0))

        heapq.heapify(minHeap)
        while k:
            element, r, c = heapq.heappop(minHeap)
            if c < n - 1:
                heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))
            k -= 1
        return element
# @lc code=end
