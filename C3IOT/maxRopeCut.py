import unittest
import sys
class Solution:
    def isValidBST(self, length: int) -> int:
        dp = [0] * (length + 1)
        dp[1] = 1
        for i in range(2, length + 1):
            for j in range(1, i//2 + 1):
                dp[i] = max(max(dp[j], j) *max(dp[i- j], (i - j)), dp[i-1])
        return dp[length]

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
print(Solution().isValidBST(3))

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
