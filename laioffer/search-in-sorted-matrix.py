class Solution:
    def search_in_sorted_matrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return [-1, -1]

        res = [-1, -1]
        m = len(matrix)
        n = len(matrix[0])

        row = self.find_row(matrix, 0, m - 1, target)
        if row == -1:
            return res

        col = self.find_col(matrix[row], 0, n -1, target)
        if col == -1:
            return res

        res = [row, col]
        return res

    def find_row(self,matrix, top, down, target):
        while top <= down:
            mid = (top + down) // 2
            if matrix[mid][0] >= target:
                down = mid - 1
            else:
                top = mid + 1
        print('top', down)
        return down

    def find_col(self,array, left, right, target):
        while left <= right:
            mid = (left + right)// 2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        print(mid)




if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    target = 5
    res = solution.search_in_sorted_matrix(matrix, target)
    print(res)
