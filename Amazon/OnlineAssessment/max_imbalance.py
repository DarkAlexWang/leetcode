def maxImBlance(arr):
    arr.sort()
    ans, n = 0, len(arr)
    for i in range(n-1):
        ans += (i + 1) * (arr[i + 1] - arr[i]) * (n - i -1)
    return ans

arr = [1,2,3]
print(maxImBlance(arr))
