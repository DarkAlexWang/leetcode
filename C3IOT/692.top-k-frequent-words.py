#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = collections.defaultdict()
        for word in words:
            dic[word] = dic.get(word, 1) + 1
        heap = []
        res = []
        for key, value in dic.items():
            heapq.heappush(heap, Word(value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word
# @lc code=end
