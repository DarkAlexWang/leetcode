class Solution:
    def max_num_n_addition(self, num, n):
        if 100 > num or num > 999:
            return -1
        if n <= 0:
            return num
        while n > 0:
            if num // 100 < 9:
                num += 100
                n -= 1
            elif num % 100 // 10 < 9:
                num += 10
                n -= 1
            else:
                num += 1
                n -= 1
        return num


if __name__ == '__main__':
    solution = Solution()
    ans = solution.max_num_n_addition(453, 7)
    print(ans)
