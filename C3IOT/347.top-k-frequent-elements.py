#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        #counter = collections.Counter(nums)
        counter = collections.defaultdict()
        for num in nums:
            counter[num] = counter.get(num, 1) + 1
        for key, value in counter.items():
            heap.append((-value, key))
        heapq.heapify(heap)
        res = []
        while k:
            value, key = heapq.heappop(heap)
            res.append(key)
            k -= 1
        return res


# @lc code=end
