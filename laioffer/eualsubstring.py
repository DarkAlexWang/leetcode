class Solution:
    def equalsubstring(self, input, fromindex, s):
        for i in range(len(s)):
            if input[fromindex + i] != s[i]
                return False

        return True

    def getallmatchs(self, input, s):
        matches = []
        i = 0
        while i < (len(input) - len(s)):
            if self.equalsubstring(input, i, s):
                matches.add(i + len(s) - 1)
                i += len(s)
            else:
                i += 1
        return matches

    def copysubstring(self, result, fromindex, t):
        for i in range(len(t)):
            result[fromindex + i] = t[i]
