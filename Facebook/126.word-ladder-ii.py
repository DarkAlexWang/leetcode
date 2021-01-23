# @lc lang=python3
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not endWord or not beginWord or not wordList or endWord not in wordList or beginWord == endWord:
            return []
        L = len(beginWord)

        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Shortest path, BFS
        res = []
        q = collections.deque()
        q.append((beginWord, [beginWord]))
        visited = set([beginWord])
        alpha = string.ascii_lowercase

        while q and not res:
            length = len(q)
            localVisited = set()
            for _ in range(length):
                word, path = q.popleft()
                for i in range(L):
                    for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
                        if nextWord == endWord:
                            res.append(path + [endWord])
                        if nextWord not in visited:
                            localVisited.add(nextWord)
                            q.append((nextWord, path + [nextWord]))
            visited = visited.union(localVisited)
        return res
