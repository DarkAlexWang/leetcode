#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        for log in logs:
            _id, event, time = log.split(":")
            if event == "start":
                if stack:
                    last = stack[-1]
                    res[last[0]] += int(time) - last[1]
                stack.append([int(_id), int(time)])
            else:
                popped = stack.pop()
                res[popped[0]] += int(time) - popped[1] + 1
                if stack:
                    stack[-1][1] = int(time) + 1
        return res
# @lc code=end
