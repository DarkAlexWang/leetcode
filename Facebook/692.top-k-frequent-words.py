## @lc lang=python3
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        min_heap = []
        for key, value in counter.items():
            heapq.heappush(min_heap, Word(value, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [heapq.heappop(min_heap).word for _ in range(k)][::-1]

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
