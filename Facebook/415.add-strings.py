# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums1, nums2 = list(num1), list(num2)
        carry, res = 0, []
        while len(nums1) > 0 or len(nums2) > 0:
            n1 = ord(nums1.pop()) - ord('0') if len(nums1) > 0 else 0
            n2 = ord(nums2.pop()) - ord('0') if len(nums2) > 0 else 0

            temp = n1 + n2 + carry

            res.append(temp % 10)

            carry = temp // 10

        if carry:
            res.append(carry)
        return "".join([str(i) for i in res])[::-1]
# @lc code=end
