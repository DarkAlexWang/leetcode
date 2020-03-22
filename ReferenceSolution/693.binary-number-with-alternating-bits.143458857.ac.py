#
# [693] Binary Number with Alternating Bits
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (55.56%)
# Total Accepted:    17K
# Total Submissions: 30.6K
# Testcase Example:  '5'
#
# Given a positive integer, check whether it has alternating bits: namely, if
# two adjacent bits will always have different values.
# 
# Example 1:
# 
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
# 
# 
# 
# Example 2:
# 
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
# 
# 
# 
# Example 3:
# 
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
# 
# 
# 
# Example 4:
# 
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.
# 
# 
#
class Solution:
    def hasAlternatingBits(self, n):
        # bit oper
        if not n:
            return False
        # XOR
        num = n ^ (n >> 1)
        
        return not (num & (num + 1))
        
