class Solution:
    #def isBalanced(self, root):
    #    if root is None:
    #        return True
    #    return self.height(root) != -1

    #def height(self, node):
    #    if node is None:
    #        return 0
    #    left = self.height(root.left)
    #    if root.left is None:
    #        return -1
    #    right = self.height(root.right)
    #    if root.right:
    #        return -1
    #    if abs(left - right) > 1:
    #        return -1

    #    return max(self.height(node.left), self.height(node.right)) + 1

    def quickSort(self, array):
        if len(array) <= 1:
            return
        low, high = 0, len(array) - 1
        self.helper(array, low, high)
        return
    def helper(self, array, low, high):
        if low < high:
            pivot = self.partition(array, low, high)
            self.helper(array, low, pivot - 1)
            self.helper(aray, pivot + 1, high)
    def partition(self, array, low, high):
        i = lwo
        j = high - 1
        while i < j:
            if array[i] < pivot:
                i += 1
            elif array[j] > pivot:
                j -= 1
            eles:
                array[i], array[j]
                i += 1
                j -= 1
            array[i], array[hgith]



# Main class function Test
if __name__ == '__main__':
    input = [2, 2, 8, 4, 5, 6, 4, 8, 8, 7]
    solution = Solution()
    ans = solution.find_duplicate(input)
    print(ans)
