#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(len(gas)):
            total_fuel = 0
            stop_count = 0
            j = i
            while stop_count < len(gas):
                total_fuel += gas[j % n] - cost[j % n]
                if total_fuel < 0:
                    break
                stop_count += 1
                j += 1
            if stop_count == len(gas) and total_fuel >= 0:
                return i
        return -1
# @lc code=end
