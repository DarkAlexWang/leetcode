#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#

# @lc code=start
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # method 1
        # Start by sorting the inputs
        horizontalCuts.sort()
        verticalCuts.sort()

        # Consider the edges first
        max_height = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            # horizontalCuts[i] - horizontalCuts[i - 1] represents the distance between
            # two adjacent edges, and thus a possible height
            max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i - 1])

        # Consider the edges first
        max_width = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            # verticalCuts[i] - verticalCuts[i - 1] represents the distance between
            # two adjacent edges, and thus a possible width
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])

        # Python doesn't need to worry about overflow - don't forget the modulo though!
        return (max_height * max_width) % (10**9 + 7)

        ## Method 2
        #horizontalCuts.sort()
        #verticalCuts.sort()
        #maxH = max(horizontalCuts[0], h - horizontalCuts[-1])
        #maxW = max(verticalCuts[0], w - verticalCuts[-1])

        #for i in range(1, len(horizontalCuts)):
        #    maxH = max(maxH, horizontalCuts[i] - horizontalCuts[i - 1])
        #for i in range(1, len(verticalCuts)):
        #    maxW = max(maxW, verticalCuts[i] - verticalCuts[i - 1])

        ##maxH = max(maxH, h - horizontalCuts[len(horizontalCuts) - 1])
        ##maxW = max(maxW, h - verticalCuts[len(verticalCuts) - 1])
        #return (maxH * maxW) % (10 ** 9 + 7)

        # method 3
        #horizontalStrips = [0] + sorted(horizontalCuts) + [h]
        #verticalStrips = [0] + sorted(verticalCuts) + [w]
        #
        #maxStripWidth = max([horizontalStrips[i + 1] - horizontalStrips[i] for i in range(len(horizontalStrips) - 1)])
        #maxStripHeight = max([verticalStrips[i + 1] - verticalStrips[i] for i in range(len(verticalStrips) - 1)])
        #
        #return (maxStripWidth * maxStripHeight) % ((10 ** 9) + 7)
# @lc code=end
