# Given a string s and an int k, return an int representing the number of
# substrings (not unique) of s with exactly k distinct characters. If the given
# string doesn't have k distinct characters, return 0.
#
# Example 1:
# Input: s = "pqpqs", k = 2
# Output: 7
# Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
# Example 2:
# Input: s = "aabab", k = 3
# Output: 0
#
# Constraints:
#
# The input string consists of only lowercase English letters [a-z]
# 0 ≤ k ≤ 26
import collections
class Solution:
    def kDistinctCharacters(self, s, k):
        return self.most_k_chars(s, k) - self.most_k_chars(s, k - 1)

    def most_k_chars(self, s, k):
        if len(s) == 0:
            return 0
        table = collections.defaultdict(int)
        num, left = 0, 0
        for i in range(len(s)):
            table[s[i]] += 1
            while len(table) > k:
                table[s[left]] -= 1
                if table[s[left]] == 0:
                    del table[s[left]]
                left += 1
            num += i - left + 1
        return num
if __name__ == "__main__":
    solution = Solution()
    out = solution.kDistinctCharacters('pqpqs', 2)
    out2 = solution.kDistinctCharacters('abcabc', 3)
    print(out2)
