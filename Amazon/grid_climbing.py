#
# Solution: Multiply the sum of nodes in current row with at least 1 node and
# the sum of nodes in the next row with at least 1 node.
#
#
def grid_climbing(grid):
    prev = 0
    connections = 0

    for row in grid:
        sum_ = 0
        for n in row:
            sum_ += n

        if sum_ > 0:
            connections += prev * sum_
            prev = sum_
    return connections

if __name__ == "__main__":
    grid = [[1, 1, 1], [0, 1, 0], [1, 1, 0]]
    print(grid_climbing(grid))
