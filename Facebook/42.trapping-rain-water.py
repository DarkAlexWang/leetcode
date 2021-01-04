#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        i = 0
        stack = []

        while i < len(height):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                # find the left bound:
                if not stack:
                    break

                distance = i - stack[-1] - 1
                bound_height = min(height[i], height[stack[-1]]) - height[top]
                res = res + distance * bound_height
            stack.append(i)
            i += 1
        return res
# @lc code=end
