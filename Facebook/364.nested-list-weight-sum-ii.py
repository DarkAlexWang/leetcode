#
# @lc app=leetcode id=364 lang=python3
#
# [364] Nested List Weight Sum II
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        level_sum = []
        for a in nestedList:
            self.dfs(a, 0, level_sum)

        for i in range(len(level_sum) -1, -1, -1):
            res += level_sum[i] * (len(level_sum) - i)

        return res

    def dfs(self, ni, depth, level_sum):
        if depth >= len(level_sum):
            for i in range(len(level_sum), depth + 1):
                level_sum.append(0)
        if ni.isInteger():
            level_sum[depth] += ni.getInteger()
        else:
            for a in ni.getList():
                self.dfs(a, depth + 1, level_sum)

# @lc code=end
