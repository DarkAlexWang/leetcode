#
# [547] Friend Circles
#
# https://leetcode.com/problems/friend-circles/description/
#
# algorithms
# Medium (49.11%)
# Total Accepted:    30.4K
# Total Submissions: 61.8K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 
# There are N students in a class. Some of them are friends, while some are
# not. Their friendship is transitive in nature. For example, if A is a direct
# friend of B, and B is a direct friend of C, then A is an indirect friend of
# C. And we defined a friend circle is a group of students who are direct or
# indirect friends.
# 
# 
# 
# Given a N*N matrix M representing the friend relationship between students in
# the class. If M[i][j] = 1, then the ith and jth students are direct friends
# with each other, otherwise not. And you have to output the total number of
# friend circles among all the students.
# 
# 
# Example 1:
# 
# Input: 
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a
# friend circle. The 2nd student himself is in a friend circle. So return 2.
# 
# 
# 
# Example 2:
# 
# Input: 
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd
# students are direct friends, so the 0th and 2nd students are indirect
# friends. All of them are in the same friend circle, so return 1.
# 
# 
# 
# 
# Note:
# 
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.
# 
# 
#

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # O(n^2), O(n)
        if not M or not M[0]:
            return 0
        
        # init
        m = len(M)
        group = [i for i in range(m)]
        count = m
        
        for i in range(m):
            for j in range(i+1, m):
                if M[i][j] == 1:
                    root1 = self.find(i, group)
                    root2 = self.find(j, group)
                    if root1 == root2:
                        pass
                    else:
                        count -= 1
                        group[root1] = root2
        return count
                        
    def find(self, e, group):
        if e == group[e]:
            return e
        else:
            return self.find(group[e], group)
        
        
