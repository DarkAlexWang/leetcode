class Solution:
    def rainbowsort(self, array):
        if len(array) <= 1:
            return
        neg = 0
        one = len(array) - 1
        zero =0
        while zero <= one:
            if array[zero] == -1:
                array[zero], array[neg] = array[neg], array[zero]
                zero +=1
                neg += 1
            elif array[zero] == 0:
                zero += 1
            else:
                array[zero], array[one] = array[one], array[zero]
                one -= 1
if __name__ == '__main__':
    input = [0, 0, 1, 1, -1, 0, -1]
    solution = Solution()
    solution.rainbowsort(input)
    print(input)
