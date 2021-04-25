def count_k_dist(s):
    n = len(s)
    distinct = len(set(s))
    result = [0] * 27
    for k in range(distinct, 1, -1):
         res = 0
         for i in range(0, n):
             dist_count = 0
             cnt = [0] * 26
             for j in range(i, n):
                 if cnt[ord(s[j]) - 97] == 0:
                     dist_count += 1
                 cnt[ord(s[j]) - 97] += 1
                 if (dist_count == k):
                     res += 1
                     print(cnt)
                 if dist_count > k:
                     break
         result[k - 1] = res + result[k]
    result[0] = n * (n + 1) // 2
    return result[:-1]
print(count_k_dist('aabc'))
