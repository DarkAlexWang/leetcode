class Solution:
    def max_prodcut(self, length):
        dp = [1] * (length + 1):
        dp[1] = 1
        for i in range(2, length + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(max(dp[j], j),* max(dp[j - 1], i - j), dp[i])
        return dp[length]
