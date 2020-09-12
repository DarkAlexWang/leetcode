class Solution:
    def sortarraythreestacks(self, s1):
        s2 = []
        s3 = []
        self.sort(s1, s2, s3, len(s1))

    def sort(self, s1, s2, s3, length):
        if length <= 1:
            return
        mid1 = length //2
        mid2 = length - length//2
        print(s1)
        for i in range(mid1):
            s2.append(s1.pop())
        self.sort(s2, s1, s3, mid1)
        self.sort(s1, s2, s3, mid2)
        i = j = 0
        while i < mid1 and j < mid2:
            if s2[-1] < s1[-1]:
                s3.append(s2.pop())
                i += 1
            else:
                s3.append(s1.pop())
                j += 1

        while i < mid1:
            s3.append(s2.pop())
            i += 1
        while j < mid2:
            s3.append(s1.pop())
            j += 1

        for i in range(length):
            s1.append(s3.pop())


if __name__ == '__main__':
    solution = Solution()
    s1 = [2, 5, 4, 6, 9, 1]
    solution.sortarraythreestacks(s1)
    print(s1)
