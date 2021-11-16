def prime_air_route(A, B, target):
    sum_arr = -1
    res = []
    for a in A:
        for b in B:
            s = a[1] + b[1]
            if s > target or s < sum_arr:
                continue
            if s > sum_arr:
                res.clear()
                sum_arr = s
            res.append({a[0], b[0]})

    return res
if __name__ == "__main__":
    ans = prime_air_route([(1,3000),(2,5000),(3,4000),(4,10000)], [(1,2000),(2,3000),(3,4000)], 11000)
    print(ans)
    ans2 = prime_air_route([(1,2000),(2,4000),(3,6000)], [(1,2000)], 7000)
    print(ans2)
