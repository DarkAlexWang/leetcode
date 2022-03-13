#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
class Solution:
    def minDeletions(self, s: str) -> int:
        st = collections.Counter(s)
        uni = set()
        count = 0
        for char, freq in st.items():
            while freq > 0 and freq in uni:
                freq -= 1
                count += 1
            uni.add(freq)
        return count

# @lc code=end
