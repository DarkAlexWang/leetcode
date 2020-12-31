#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        arry = list(str(num))
        last = {int(x): i for i, x in enumerate(arry)}
        print(last)
        for i, x in enumerate(arry):
            for d in range(9, int(x), -1):
                if last.get(d, 0) > i:
                    arry[i], arry[last[d]] = arry[last[d]], arry[i]
                    return int("".join(arry))


# @lc code=end
