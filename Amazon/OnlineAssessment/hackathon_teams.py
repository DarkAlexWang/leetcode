class Solution:
    def CountMaxTeams(self, skills, teamSize: int, maxDiff: int) -> int:
        # edge case
        if len(skills) < teamSize:
            return 0
        if len(skills) == 1:
            return 1
        skills.sort()
        res = 0
        start = 0
        end = start + teamSize - 1
        while end < len(skills):
            if skills[end] - skills[start] <= maxDiff:
                res = res + 1
                start = end + 1
                end = start + teamSize - 1
            else:
                start = start + 1
                end = end + 1

        return res

if __name__ == "__main__":
	solution = Solution()
	ans1 = solution.CountMaxTeams([3, 4, 3, 1, 6, 5], 3, 2)
	print(ans1)
