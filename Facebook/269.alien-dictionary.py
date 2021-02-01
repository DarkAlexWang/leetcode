# @lc lang=python3
class Solution:
    def alienOrder(self, words):
        res = []
        indegree, outdegree = collections.defaultdict(int), collections.defaultdict(list)

        q = collections.deque()

        for i in range(1, len(words)):
            if len(words[i -1]) > len(words[i]) and words[i - 1][:len(words[i])] == words[i]:
                continue
            self.buildToplogicalSort(words[i -1], words[i], indegree, outdegree)

        if not outdegree and len(words) == 2 and len(words[0]) > len(words[1]):
            return ''

        nodes = set()
        for word in words:
            for char in word:
                nodes.add(char)

        for char in nodes:
            if indegree[char] == 0:
                q.append(char)

        while q:
            prev = q.popleft()
            res.append(prev)

            for succ in outdegree[prev]:
                indegree[succ] -= 1
                if indegree[succ] == 0:
                    q.append(succ)

            del(outdegree[prev])

        if outdegree:
            return ""
        return "".join(res)

    def buildToplogicalSort(self, word1, word2, indegree, outdegree):
        length = min(len(word1), len(word2))
        for i in range(length):
            if word1[i] != word2[i]:
                if word2[i] not in outdegree[word1[i]]:
                    indegree[word2[i]] += 1
                    outdegree[word1[i]].append(word2[i])
                break
