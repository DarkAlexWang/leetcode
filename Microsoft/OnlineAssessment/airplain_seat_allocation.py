#
# Microsoft Airplane allocation question
# input N and S
#
import collections
class Solution:
    def maxNumberOfFamilies(self, N, S):
        seats = collections.defaultdict(set)
        res = 2 * N
        if S == '':
            return res
        S = S.split(' ')
        reservedSeats = []
        for elem in S:
            reservedSeats.append((int(elem[0]), elem[1]))

        import ipdb; ipdb.set_trace() # BREAKPOINT

        for i, j in reservedSeats:
            if j in ['B', 'C', 'D', 'E']:
                seats[i].add(0)
            if j in ['D', 'E', 'F', 'G']:
                seats[i].add(1)
            if j in ['F', 'G', 'H', 'J']:
                seats[i].add(2)
        for i in seats:
            if len(seats[i]) == 3:
                res -= 2
            else:
                res -= 1
        return res

if __name__ == "__main__":
    solution = Solution()
    ans1 = solution.maxNumberOfFamilies(2, '')
    print(ans1)
    ans2 = solution.maxNumberOfFamilies(3, '1A 1D 2E 2G')
    print(ans2)
