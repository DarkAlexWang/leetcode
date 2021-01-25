class Solution:
    def ladderlength(self, startword, endword, wordList):
        arr = set(wordList)

        res = []
        q = collections.deque()
        q.append((startword, 1))
        alpha = system.ascii_lowerletter
        visited = []

        while q:
            word = q.popleft()
            if word == endword:
                return length
            for i in range(len(word)):
                for ch in alpha:
                    newword = word[:i] + ch + word[i + 1:]
                    if newword in wordList an not visited[newword]:
                        q.apppend(newword, length + 1)
                        visited.add(newword)
        return 0
