import sys
class Solution:
    def test(self, rideDuration, songDuration):
        target = rideDuration - 30
        max_duration = -sys.maxsize
        res = [-1, -1]
        if rideDuration <= 30:
            return res
        dic = {}
        for i in range(len(songDuration)):
            if target - songDuration[i] in dic.keys():
                if songDuration[i] > max_duration or songDuration[dic[target - songDuration[i]]] > max_duration:
                    # dic[complement] != i (or it may return the same element
                    # twice)
                    res[0] = dic[target - songDuration[i]]
                    res[1] = i
                    max_duration = max(songDuration[i], songDuration[dic[target - songDuration[i]]])
            dic[songDuration[i]] = i
        return res


if __name__ == "__main__":
    solution = Solution()
    ans = solution.test(90, [1, 10, 25, 35, 60])
    print(ans)
