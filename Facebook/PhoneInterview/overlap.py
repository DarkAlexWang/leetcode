# Python3 program that print maximum
# number of overlap
# among given ranges

# Function that prmaximum
# overlap among ranges
def overlap(v):

    # variable to store the maximum
    # count
    ans = 0
    count = 0
    data = []

    # storing the x and y
    # coordinates in data vector
    for i in range(len(v)):

        # pushing the x coordinate
        data.append([v[i][0], 'x'])

        # pushing the y coordinate
        data.append([v[i][1], 'y'])

    # sorting of ranges
    data = sorted(data)

    # Traverse the data vector to
    # count number of overlaps
    for i in range(len(data)):

        # if x occur it means a new range
        # is added so we increase count
        if (data[i][1] == 'x'):
            count += 1

        # if y occur it means a range
        # is ended so we decrease count
        if (data[i][1] == 'y'):
            count -= 1

        # updating the value of ans
        # after every traversal
        ans = max(ans, count)

    # printing the maximum value
    print(ans)

# Driver code
v = [ [ 1, 2 ], [ 2, 4 ], [ 3, 6 ] ]
overlap(v)
