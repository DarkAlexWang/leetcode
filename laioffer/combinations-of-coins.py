#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = []
        path = []
        if len(coins) == 0 and amount == 0:
            return 1
        if len(coins) == 0 and amount != 0:
            return 0
        self.dfs(amount, coins, len(coins) -1, path, res)
        answer = len(res)
        return answer

    def dfs(self, amount, coins, index, path, res):
        if index == 0:
            if amount % coins[0] == 0:
                path.append(amount//coins[0])
                res.append(path)
                path = path[:-1]
            return
        maxnumber = amount // coins[index]
        for i in range(maxnumber + 1):
            path.append(i)
            self.dfs(amount - i * coins[index], coins, index - 1, path, res)
            path = path[:-1]
# @lc code=end
