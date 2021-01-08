# @lc lang=python3
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}':'{'}
        stack = []
        for char in s:
            if char in dic.values():
                stack.append(char)
            elif char in dic.keys():
                if stack == [] or stack.pop() != dic[char]:
                    return False
            else:
                return False
        return stack == []
