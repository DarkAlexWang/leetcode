class GCD:
    def solution(self, arry):
        if arry == None or len(arry) == 1:
            return 0
        gcd = arry[0]
        for i in range(1, len(arry)):
            gcd = self.greatest_common_divisor(gcd, arry[i])
        return gcd
    def greatest_common_divisor(self, num1, num2):
        if num1 == 0 or num2 == 0:
            return 0
        while num1 != 0 and num2 != 0:
            if num2 > num1:
                num1 ^= num2
                num2 ^= num1
                num1 ^= num2
            tmp = num1 % num2
            num1 = num2
            num2 = tmp
        return num1 + num2

if __name__ == "__main__":
    GCD = GCD()
    res = GCD.solution([4, 2, 6, 8, 10])
    print(res)
