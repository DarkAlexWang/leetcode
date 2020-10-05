#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
from collections import defaultdict
from heapq import heappush, heappop

class WordFreq:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq.__lt__(other.freq)
        else:
            return self.word.__gt__(other.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int):
        if len(words) == 0:
            return ""
        freqmap = defaultdict(int)
        for word in words:
            freqmap[word] += 1

        k_most_frequent = []
        for word , freq in freqmap.items():
            heappush(k_most_frequent, WordFreq(freq, word))
            if len(k_most_frequent) == k + 1:
                heappop(k_most_frequent)

        res = []
        while len(k_most_frequent) != 0:
            res.insert(0, heappop(k_most_frequent).word)
        return res
# @lc code=end
