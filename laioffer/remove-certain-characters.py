class Solution:
    def remove(self, string, t):
        array = list(string)
        uniq_t = set(t)

        slow = 0
        fast = 0
        for fast in range(0, len(array)):
            if array[fast] not in uniq_t:
                array[slow] = array[fast]
                slow += 1
        res = ""
        for i in range(slow):
            res += array[i]
        return res

if __name__ == "__main__":
    solution = Solution()
    res = solution.remove("aaabbbccc", "a")
    print(res)
