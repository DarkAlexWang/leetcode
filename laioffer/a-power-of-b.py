class Solution:
    def power(self, a, b):
        if b == 0:
            return 1
        if a == 0:
            return 0
        half = pow(a, b//2)
        return half * half if b%2 == 0 else half* half * a

if __name__ == '__main__':
    solution = Solution()
    res = solution.power(2, 3)
    print(res)
