class Solution:
    def min_duplicate_string(self, s):
        dup = set()
        count = 1
        for char in s:
            if char in dup:
                count += 1
                dup.clear()
                dup.add(char)
            else:
                dup.add(char)
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.min_duplicate_string('abbbbcca'))
