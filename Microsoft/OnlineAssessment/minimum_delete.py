class Solution:
    def minimum_delete(self, s):
        aSum, bSum = 0, 0
        for c in s:
            if c == 'A':
                aSum += 1
            else:
                aSum = min(aSum, bSum)
                bSum += 1
        return min(aSum, bSum)



if __name__ == "__main__":
    solution = Solution()
    ans = solution.minimum_delete('BAAABAB')
    print(ans)
