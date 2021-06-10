# @lc lang=python3
class Solution:
    def alienOrder(self, words):
        res = []
        indegree, outdegree = collections.defaultdict(int), collections.defaultdict(list)

        q = collections.deque()

        for i in range(1, len(words)):
            #consider case "play and playing"
            if len(words[i -1]) > len(words[i]) and words[i - 1][:len(words[i])] == words[i]:
                continue
            self.buildToplogicalSort(words[i -1], words[i], indegree, outdegree)

        # Take care so some corner cases
        if not outdegree and len(words) == 2 and len(words[0]) > len(words[1]):
            return ''

        # build number of char
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
            # we need to check outdegree because we del outdegree if we find

            for succ in outdegree[prev]:
                indegree[succ] -= 1
                if indegree[succ] == 0:
                    q.append(succ)
            # del outdegree for this char
            del(outdegree[prev])

        if outdegree:
            return ""
        return "".join(res)

    def buildToplogicalSort(self, word1, word2, indegree, outdegree):
        length = min(len(word1), len(word2))
        for i in range(length):
            if word1[i] != word2[i]:
                # init pre char
                # if word1[i] not in outdegree:
                #       outdegree[word1[i]] = set()
                if word2[i] not in outdegree[word1[i]]:
                    indegree[word2[i]] += 1
                    outdegree[word1[i]].append(word2[i])
                # only contain two char is not the same its order after that is irrelevent
                break
