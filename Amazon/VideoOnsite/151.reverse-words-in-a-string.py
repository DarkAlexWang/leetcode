#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        self.reverse_string(arr, 0, len(arr) - 1)
        self.reverse_word(arr)
        word = self.trim_sides(arr)
        res = self.trim_space(word)
        return ''.join(res)

    def reverse_string(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr

    def reverse_word(self, arr):
        l, r = 0, 0
        while r < len(arr):
            while r < len(arr) and not arr[r].isspace():
                r += 1
            self.reverse_string(arr, l, r - 1)
            r += 1
            l = r
        return arr

    def trim_sides(self, arr):
        if ''.join(arr).isspace():
            return []
        l, r = 0, len(arr) - 1
        while l < r and arr[l].isspace():
            l += 1
        while l < r and arr[r].isspace():
            r -= 1
        return arr[l:r + 1]

    def trim_space(self, word):
        if not word:
            return []
        res = [word[0]]
        for i in range(1, len(word)):
            if res[-1].isspace() and word[i].isspace():
                continue
            res.append(word[i])
        return res


# @lc code=end
