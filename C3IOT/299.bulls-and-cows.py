#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dict = collections.defaultdict(int)
        guess_dict = collections.defaultdict(int)

        A, B = 0, 0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                A += 1
            else:
                secret_dict[secret[i]] += 1
                guess_dict[guess[i]] += 1
        for ele in guess_dict:
            B += min(guess_dict[ele], secret_dict[ele])
        result = '%dA%dB' %(A, B)
        return result
# @lc code=end
