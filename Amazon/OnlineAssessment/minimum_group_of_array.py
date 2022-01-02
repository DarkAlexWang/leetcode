def minimum_group_of_array(arr, k):
    arr.sort()
    idx = 0
    res = 1
    for i in range(len(arr)):
        if arr[i] - arr[idx] > k:
            res += 1
            idx = i
    return res

if __name__ == "__main__":
    print(minimum_group_of_array([4, 3, 2, 1, 6], 2))
