#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        countList = [0] * 26
        booleanList = [False] * 26
        stack = []
        for char in s:
            countList[ord(char) - ord('a')] += 1

        for char in s:
            countList[ord(char) - ord('a')] -= 1
            if booleanList[ord(char) - ord('a')]:
                continue
            while stack and  char < stack[-1] and countList[ord(stack[-1]) - ord('a')] > 0:
                booleanList[ord(stack[-1]) - ord('a')] = False
                stack.pop()
            stack.append(char)
            booleanList[ord(stack[-1]) - ord('a')] = True
        return ''.join(stack)
# @lc code=end
