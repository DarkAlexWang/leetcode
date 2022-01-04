#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l // 2)
        else:
            return (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l// 2 -1)) / 2

    def kth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        i_nums1, i_nums2 = len(nums1) // 2, len(nums2) // 2
        m_nums1, m_nums2 = nums1[i_nums1], nums2[i_nums2]

        if i_nums1 + i_nums2 < k:
            if m_nums1 > m_nums2:
                return self.kth(nums1, nums2[i_nums2 + 1:], k - i_nums2 - 1)

            else:
                return self.kth(nums1[i_nums1 + 1:], nums2, k - i_nums1 - 1)
        else:
            if m_nums1 > m_nums2:
                return self.kth(nums1[:i_nums1], nums2, k)

            else:
                return self.kth(nums1, nums2[:i_nums2], k)
# @lc code=end
