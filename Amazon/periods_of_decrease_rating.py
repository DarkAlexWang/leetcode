class Solution:
    def periodsOfDecreaseRating(self, ratings):
        """
        Brute force O(n^2) approach
        """
        res = 0
        i = 0
        m = len(ratings)

        for i in range(m):
            cur = 1
            prev = ratings[i]
            j = i + 1
            while j < m and prev > ratings[j]:
                cur += 1
                prev = ratings[j]
                j += 1
            res += cur
        return res

    def periodsOfDecreaseRating2(self, ratings):
        """
        two pointer O(n) approach
        """
        res = 0
        i = 0
        m = len(ratings)

        for j in range(m):
            if j > 0 and ratings[j] < ratings[j - 1]:
                res += j - i + 1
            else:
                res += 1
                i = j
        return res

sol = Solution()
print(sol.periodsOfDecreaseRating2([4,3,5,4,3])) # ret 9
print(sol.periodsOfDecreaseRating2([3,2,1])) # ret 6
print(sol.periodsOfDecreaseRating2([9, 8, 7, 6, 5]))  # ret 15
