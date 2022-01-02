#class Solution:
#    def maximum_overlap(self, v):
#        # variable to store the maximum
#        # count
#        ans = 0
#        count = 0
#        data = []
#
#        # storing the x and y
#        # coordinates in data vector
#        for i in range(len(v)):
#
#            # pushing the x coordinate
#            data.append([v[i][0], 'x'])
#
#            # pushing the y coordinate
#            data.append([v[i][1], 'y'])
#
#            # sorting of ranges
#        data = sorted(data)
#
#        # Traverse the data vector to
#        # count number of overlaps
#        for i in range(len(data)):
#
#            # if x occur it means a new range
#            # is added so we increase count
#            if (data[i][1] == 'x'):
#            	count += 1
#
#            # if y occur it means a range
#            # is ended so we decrease count
#            if (data[i][1] == 'y'):
#            	count -= 1
#
#            # updating the value of ans
#            # after every traversal
#            ans = max(ans, count)
#
#        # printing the maximum value
#        return ans


class Solution:
    def maximum_overlap(self, logs):
        windows = []
        for begin, end in logs:
            windows.append((begin, 1, end))
            windows.append((end, -1, 0))

        windows.sort()

        cur_length = 0
        count = 0
        max_count = 1
        res = 0

        for num, flag, key in windows:
            count += flag
            if count > max_count:
                max_count = count
                cur_length = key - num + 1
                res = cur_length

        return res



# Driver code
if __name__ == "__main__":
    solution = Solution()
    v = [ [ 1, 2 ], [ 2, 4 ], [ 3, 6 ] ]
    v2 = [ [ 1, 10 ], [ 2, 8 ], [ 3, 4 ] ]
    v3 = [ [ 1, 4 ], [ 2, 5 ], [ 9, 12 ], [5, 9], [5, 12] ]
    print(solution.maximum_overlap(v3))
