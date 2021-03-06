import unittest
import sys
#class Solution:
#    def maxSubArray(self, nums):

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        res = left = 0
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = dict.get(s[i], 0) + 1
            while len(dict) > 2:
                print(len(dict))
                dict[s[left]] -= 1
                if dict[s[left]] == 0:
                    del dict[s[left]]
                    left += 1
            res = max(res, i - left + 1)

        return res


## UnitTest Function
#class TestSolution(unittest.TestCase):
#    def test_none_1(self):
#        input = 1
#        self.assertTrue(Solution().isValidBST(input))
#    def main(self):
#        input = 12
#        self.assertTrue(Solution().isValidBST(input))
#        print(isValidBST(input))
#if __name__ == "__main__":
#    unittest.main()

## Single Print Testing
print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))

## Main class function Test
#class Main():
#    def main(self):
#        input = 12
#        res = Solution().isValidBST(input)
#        print(res)
#Main.main(12)
   # if __name__ == '__main__':
   #     if len(sys.argv) > 1:
   #         main(int(sys.argv[1]))
