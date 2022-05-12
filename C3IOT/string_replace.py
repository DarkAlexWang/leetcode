class Solution:
    def string_replace(self, string, s, t):
        array = list(string)
        if len(s) >= len(t):
            return self.replace_shorter(array, s, t)
        return self.replace_longer(array, s, t)
    def replace_shorter(self, array, s, t):
        slow = 0
        fast = 0
        while fast < len(array):
            if fast <= len(array) - len(s) and self.equal_substring(array, fast, s):
                self.copySubstring(array, slow, t)
                slow += len(t)
                fast += len(s)
            else:
                array[slow] = array[fast]
                slow += 1
                fast += 1
        return "".join(array[:slow])

    def replace_longer(self, array, s, t):
        matches = self.getAllMatches(array, s)
        res = [''] * (len(array) + len(matches) * (len(t) - len(s)))
        lastIndex = len(matches) - 1
        slow = len(array) - 1
        fast = len(res) - 1
        while slow >= 0:
            if lastIndex >= 0 and slow == matches[lastIndex]:
                self.copySubstring(res, fast - len(t) + 1, t)
                fast -= len(t)
                slow -= len(s)
                lastIndex -= 1
            else:
                res[fast] = array[slow]
        return "".join(res)
    def equal_substring(self, array, fromIndex, s):
        for i in range(len(s)):
            if array[fromIndex + i] != s[i]:
                return False
        return True

    def copySubstring(self, res, fromIndex, t):
        for i in range(len(t)):
            res[fromIndex + 1] = t[i]


    def getAllMatches(self, array,s):
        matches = []
        i = 0
        while i < len(array) - len(s):
            if self.equal_substring(array, i, s):
                matches.append(i + len(s) - 1)
                i += len(s)
            else:
                i += 1
        return matches


if __name__ == "__main__":
    solution = Solution()
    ans = solution.string_replace('abscdged', 'cd', 'xxxx')
    print(ans)
