#
# @lc app=leetcode id=1086 lang=python3
#
# [1086] High Five
#

# @lc code=start
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        result = []
        dic = collections.defaultdict(list)
        for idx, val in items:
            heapq.heappush(dic[idx], val)
            if len(dic[idx]) > 5:
                heapq.heappop(dic[idx])

        result = [[i, sum(dic[i]) // len(dic[i])] for i in sorted(dic)]
        return result
# @lc code=end
