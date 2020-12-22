#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        listFinal = []
        # Base case.
        if '+' not in input and '-' not in input and '*' not in input:
            listFinal.append(int(input))

        # Recursive case
        for i, v in enumerate(input):
            if v == '+' or v == '-' or v == "*":
                listFirst = self.diffWaysToCompute(input[0:i])
                listSecond = self.diffWaysToCompute(input[i +1: len(input)])
                for i, valuei in enumerate(listFirst):
                    for j, valuej in enumerate(listSecond):
                        if v == '+':
                            listFinal.append(valuei + valuej)
                        elif v == '-':
                            listFinal.append(valuei - valuej)
                        else:
                            listFinal.append(valuei * valuej)
        return listFinal



# @lc code=end
