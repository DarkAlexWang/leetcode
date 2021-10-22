#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i,j):
            pi, pj = find(i), find(j)
            if pi != pj:
                if rank[pi] >= pj:
                    parent[pj] = pi
                    rank[pi] += 1
                else:
                    parent[pi] = pj
                    rank[pj] += 1

        if not nums:
            return 0 # corner case

        # first pass is initialize parent and rank for all num in nums
        parent, rank, nums = {}, {}, set(nums)
        for num in nums: # init
            parent[num] = num
            rank[num] = 0

        # second pass: union nums[i] with nums[i]-1 and nums[i]+1 if ums[i]-1 and nums[i]+1 in nums
        for num in nums:
            if num-1 in nums:
                union(num-1, num)
            if num+1 in nums:
                union(num+1, num)

        # second pass find numbers under the same parent
        d = collections.defaultdict(list)
        for num in nums:
            d[find(num)].append(num)
        return max([len(l) for l in d.values()])
# @lc code=end
