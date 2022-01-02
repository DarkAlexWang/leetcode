import sys
class Solution:
    def minimal_flips(self, coins):
        n = len(coins)
        # two arrays will keep the count for number of T and H to be flipped
        # while traversing from left to right and right to left respectively
        flipsFromLeft = [0 for _ in range(n)]
        flipsFromRight = [0 for _ in range(n)]

        # Fill flipsFromLeft
        flips = 0
        for i in range(n):
            if coins[i] == 'T':
                flips += 1
            flipsFromLeft[i] = flips
        if flips == 0:
            return 0


        # Fill flipsFromRight
        flips = 0
        for i in range(n - 1, -1, -1):
            if coins[i] == 'H':
                flips += 1

            flipsFromRight[i] = flips
        if flips == 0:
            return 0

        # Initialize minFlip to highest int value. If sum of leftflip and
        # rightFlip is smaller than minFlips, then update minFlips
        minFlips = sys.maxsize
        for i in range(1, n):
            if flipsFromLeft[i - 1] + flipsFromRight[i] < minFlips:
                minFlips = flipsFromLeft[i - 1] + flipsFromRight[i]
        return minFlips

if __name__ == "__main__":
    solution = Solution()
    res1 = solution.minimal_flips('HHTHTT')
    print(res1)
    res2 = solution.minimal_flips('HHH')
    print(res2)
