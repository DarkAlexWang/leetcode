#
# [195] Tenth Line
#
# https://leetcode.com/problems/tenth-line/description/
#
# shell
# Easy (33.49%)
# Total Accepted:    25K
# Total Submissions: 74.5K
# Testcase Example:  'Line 1\\nLine 2\\nLine 3\\nLine 4\\nLine 5\\nLine 6\\nLine 7\\nLine 8\\nLine 9\\nLine 10'
#
# How would you print just the 10th line of a file?
# 
# For example, assume that file.txt has the following content:
# 
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
# 
# 
# Your script should output the tenth line, which is:
# 
# Line 10
# 
# 
# [show hint]
# Hint:
# 1. If the file contains less than 10 lines, what should you output?
# 2. There's at least three different solutions. Try to explore all
# possibilities.
# 
#
# Read from the file file.txt and output the tenth line to stdout.
sed -n 10p file.txt
