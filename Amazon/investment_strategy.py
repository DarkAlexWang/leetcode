class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for update in updates:
            start, end, inc = update
            res[start] += inc

            if end + 1 <= length - 1:
                res[end+1] -= inc

        sum = 0
        for i in range(length):
            sum += res[i]
            res[i] = sum
        return max(res)

if __name__ == "__main__":
    solution = Solution()
    ans1 = solution.getModifiedArray(5, [[1, 2, 10], [2, 4, 5], [3, 5, 12]])
    print(ans1)
