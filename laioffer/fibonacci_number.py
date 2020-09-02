class Solution:
    def fibonacci_number(self, k):
        if k <= 0:
            return 0
        if k == 1:
            return 1
        return fibonacci_number(k-1) + fibonacci_number(k- 2)

    def fibonacci_number2(self, k):
        if k <= 0:
            return 0
        array = [0]*(k + 1)
        array[1] = 1
        for i in range(2, k + 1):
            array[i] = array[i-1] + array[i - 2]
        return array[k]

if __name__ == '__main__':
    solution = Solution()
    res = solution.fibonacci_number2(3)
    print(res)
