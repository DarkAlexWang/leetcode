class Solution:
    def rightshift(self, string, n):
        if len(string)< 1:
            return string
        arry = list(string)
        n %= len(arry)
        self.reverse(arry, len(arry) - n, len(arry) - 1)
        self.reverse(arry, 0, len(arry) - n - 1)
        self.reverse(arry, 0, len(arry) - 1)

        return ''.join(arry)

    def reverse(self, arry, l, r):
        while l < r:
            tmp = arry[l]
            arry[l] = arry[r]
            arry[r] = tmp
            l += 1
            r -= 1


if __name__ == "__main__":
    solution = Solution()
    res = solution.rightshift("abcdef", 2)
    print(res)
