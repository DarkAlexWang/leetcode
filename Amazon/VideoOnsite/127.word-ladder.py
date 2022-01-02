#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        arr = set(wordList) # avoid TLE
        q = collections.deque([(beginWord, 1)])
        visited = set()
        alpha = string.ascii_lowercase
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for ch in alpha:
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word in arr and new_word not in visited:
                        q.append((new_word, length + 1))
                        visited.add(new_word)
        return 0

# @lc code=end
