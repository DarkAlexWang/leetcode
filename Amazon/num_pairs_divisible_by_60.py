#1. get the remainders of each elements
#2. count the number of each reamainders
#3. analyze the counts to find the valid pair
# The time complexity is O(N), and space complexity is O(1)
class Solution:
    def num_pairs_divisible_by_60(self, time):
        res = 0
        rem = [0 for _ in range(60)]
        for t in time:
            rem[t % 60] += 1
        for i in range(1, 30):
            res += rem[i] * rem[60 - i]
        res += rem[0] * (rem[0] - 1) // 2 + rem[30] * (rem[30] - 1) // 2
        return res

if __name__ == "__main__":
    solution = Solution()
    ans1 = solution.num_pairs_divisible_by_60([60, 21, 60, 60])
    print(ans1)
