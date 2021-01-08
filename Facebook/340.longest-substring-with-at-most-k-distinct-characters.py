# @lc lang=python3
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        freq = Counter()

        start = 0

        longest_substring = 0

        for window_end, char in enumerate(s):
            freq[char] += 1
            while len(freq)  > k:

                left_char = s[start]

                freq[left_char] -= 1

                if freq[left_char] == 0:
                    del freq[left_char]
                start += 1

            window_size = window_end - start + 1
            longest_substring = max(longest_substring, window_size)
        return longest_substring
