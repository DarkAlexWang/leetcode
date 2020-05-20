#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while stack and k > 0:
                if stack[-1] > num[i]:
                    k -= 1
                    stack.pop()
                else:
                    break
            stack.append(num[i])

        while k > 0:
            stack.pop()
            k -= 1

        while stack:
            if stack[0] == '0':
                stack = stack[1:]
            else:
                break
        return ''.join(stack) or '0'
# @lc code=end
