#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#

# @lc code=start
# Count the occurrences of each number using HashMap;
# Using TreeMap to count each occurrence;
# Poll out currently least frequent elemnets, and check if reaching k, deduct
# the correponding unique count remaining.
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = collections.Counter(arr)
        cnt, remaining = collections.Counter(c.values()), len(c)
        for key in sorted(cnt):
            if k >= key * cnt[key]:
                k -= key * cnt[key]
                remaining -= cnt.pop(key)
            else:
                return remaining - k // key
        return remaining

# @lc code=end
