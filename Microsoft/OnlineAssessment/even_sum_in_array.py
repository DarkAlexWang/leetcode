class Solution:
    def even_sum_in_array(self, arr):
        count = 0
        #arr_set = set()
        #for i in range(1, len(arr)):
        #    sum_ = arr[i -1] + arr[i]
        #    if sum_ % 2 == 0 and (arr[i - 1], arr[i]) not in arr_set and (arr[i], arr[i - 1]) not in arr_set:
        #        arr_set.add((arr[i - 1], arr[i]))
        #        count += 1
        #    elif i == len(arr) - 1 and (arr[0] + arr[i]) % 2 == 0:
        #        count += 1
        #    else:
        #        continue
        #return count
        i = 1
        while i < len(arr):
            sum_ = arr[i] + arr[i - 1]
            if sum_ % 2 == 0:
                count += 1
                i += 2
            else:
                i += 1
        if (arr[0] + arr[-1]) % 2 == 0 and (arr[0] + arr[1]) % 2 != 0:
            count += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    ans = solution.even_sum_in_array([2, 5, 8, 7, 3, 7, 4])
    print(ans)
