class Solution:
    def getModifiedArray(self, length, updates):
        ans = [0] * length
        for start, end, value in updates:
            ans[start] += value
            end += 1
            if end < len(ans):
                ans[end] -= value

        for i in range(1, len(ans)):
            ans[i] += ans[i - 1]
        return ans
