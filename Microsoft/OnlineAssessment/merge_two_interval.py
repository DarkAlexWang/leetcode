"""
Merge two sorted (ascending) lists of interval and return it as a new
sorted list. The new sorted list should be made by splicing together the
intervals of the two lists and sorted in ascending order.
"""
class Solution:
    #def merge_two_interval(self, list1, list2):
    #    if not list1 or not list2:
    #        return list1 or list2

    #    list1.sort(key = lambda x: x[0])
    #    list2.sort(key = lambda x: x[0])
    #    res = []
    #    i = j = 0

    #    if list1[0][0] < list2[0][0]:
    #        prev = list1[0]
    #        i = 1
    #    else:
    #        prev = list2[0]
    #        j = 1
    #    while i < len(list1) or j < len(list2):
    #        if j == len(list2) or (i < len(list1) and list1[i][0] < list2[j][0]):
    #            if prev[1] < list1[i][0]:
    #                res.append(prev)
    #                prev = list1[i]
    #            else:
    #                prev[1] = max(prev[1], list1[i][1])
    #            i += 1
    #        else:
    #            if prev[1] < list2[j][0]:
    #                res.append(prev)
    #                prev = list2[j]
    #            else:
    #                prev[1] = max(prev[1], list2[j][1])
    #            j += 1
    #    res.append(prev)
    #    return res

    def merge_two_interval(self, l1, l2):
        i = j = 0
        res = []
        while i < len(l1) or j  < len(l2):
            if i == len(l1):
                curr = l2[j]
                j += 1
            elif j == len(l2):
                curr = l2[i]
                i += 1
            elif l1[i][0] < l2[j][0]:
                curr = l1[i]
                i += 1
            else:
                curr = l2[j]
                j += 1
            if res and res[-1][-1] >= curr[0]:
                res[-1][-1] = max(res[-1][-1], curr[-1])
            else:
                res.append(curr)
        return res



if __name__ == "__main__":
    solution = Solution()
    ans1 = solution.merge_two_interval([[1, 2], [3, 4]], [[2, 3], [5, 6]])
    print(ans1)
