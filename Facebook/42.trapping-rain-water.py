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

    def trap2(self, height: List[int]) -> int:
        n = len(height)

        left_bracket = [height[0] for i in range(n)]
        right_bracket = [height[-1] for i in range(n)]

        for i in range(1, n):
            left_bracket[i] = max(left_bracket[i - 1], height[i])
        for i in range(n - 1, -1, -1):
            right_bracket[i] = max(right_bracket[i + 1], height[i])

        water = 0
        for i in range(n):
            water += min(left_bracket[i], right_bracket[i]) - height[i]
        return water
# @lc code=end
