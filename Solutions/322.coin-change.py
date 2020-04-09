#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
         coins.sort(reverse = True)
         min_coins = float('inf')

         def count_coins(start_coin, coin_count, remaining_amount):
             nonlocal min_coins
             if remaining_amount == 0:
                 min_coins = min(min_coins, coin_count)
                 return
             for i in range(start_coin, len(coins)):
                 remaining_coin_allowance = min_coins - coin_count
                 max_amount_possible = coins[i] * remaining_coin_allowance
                 if coins[i] <= remaining_amount and remaining_amount < max_amount_possible:
                     count_coins(i, coin_count+1, remaining_amount - coins[i])
         count_coins(0, 0, amount)
         return min_coins if min_coins < float('inf') else -1
# @lc code=end
#
