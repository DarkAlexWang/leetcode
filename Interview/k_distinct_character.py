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
        if len(s) == 0:
            return 0

        n = len(s)
        num_of_substrings = 0
        different_chars = 0
        counter = collections.defaultdict(int)
        j = 0
        resultset = set()
        for i in range(n):
            while j < n and different_chars < k:
                counter[s[j]] += 1
                if counter[s[j]] == 1:
                    different_chars += 1
                j += 1

            if different_chars == k:
                resultset.add(s[i:j])
            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                different_chars -= 1
        num_of_substrings = len(resultset)
        print(resultset)
        return num_of_substrings


if __name__ == "__main__":
    solution = Solution()
    out = solution.kDistinctCharacters('abacab', 3)
    print(out)
