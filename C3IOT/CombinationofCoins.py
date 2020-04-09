'''
Given a number of different denominations of coins (e.g., 1 cent, 5 cents, 10 cents, 25 cents), get all the possible ways to pay a target number of cents.

Arguments

coins - an array of positive integers representing the different denominations of coins, there are no duplicate numbers and the numbers are sorted by descending order, eg. {25, 10, 5, 2, 1}
target - a non-negative integer representing the target number of cents, eg. 99
Assumptions

coins is not null and is not empty, all the numbers in coins are positive
target > = 0
You have infinite number of coins for each of the denominations, you can pick any number of the coins.
Return

a list of ways of combinations of coins to sum up to be target.
each way of combinations is represented by list of integer, the number at each index means the number of coins used for the denomination at corresponding index.
Examples

coins = {2, 1}, target = 4, the return should be

[

    [0, 4], (4 cents can be conducted by 0 * 2 cents + 4 * 1 cents)

    [1, 2], (4 cents can be conducted by 1 * 2 cents + 2 * 1 cents)

    [2, 0] (4 cents can be conducted by 2 * 2 cents + 0 * 1 cents)


]

Solution: 每层代表coin type，每层loop through该硬币可用的个数
'''

Class Solution1(object):
    def combinationCoins(self, target, coins):
        n = len(coins)
        if level == n:
            sol[level] = money_left
            return sol
    def findCombination(self, money_left, level, coins, sol):
        for i <= money_left/coins[level]:
            sol[level] = i
            self.findCombination(money_left -i * coins[level], level + 1, sol)


        if level >= len(coins):
            if remaining == 0:
                res.append(path)

Class Solution2(object):
  def coinChange(self, coins: List[int], amount: int) -> int:
    coins.sort(reverse = True)
    min_coins = float('inf')

    def count_coins(start_coin, coin_count, remaining_amount):
      nonlocal min_coins

      if remaining_amount == 0:
        min_coins = min(min_coins, coin_count)
        return

      # Iterate from largest coins to smallest coins
      for i in range(start_coin, len(coins)):
        remaining_coin_allowance = min_coins - coin_count
        max_amount_possible = coins[i] * remaining_coin_allowance

        if coins[i] <= remaining_amount and remaining_amount < max_amount_possible:
          count_coins(i, coin_count + 1, remaining_amount - coins[i])

    count_coins(0, 0, amount)
    return min_coins if min_coins < float('inf') else -1
