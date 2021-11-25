from collections import defaultdict

def strength_pwd(s: str):
    dic = defaultdict(lambda: (0,0))
    prev = 0
    ans = 0
    for i,ch in enumerate(s):
        cur = prev+i+1
        dic[ch] = (i + 1, dic[ch][1] + dic[ch][0])
        ans += cur - sum([dic[k][1] for k in dic])
        prev = cur

    return ans


if __name__ == '__main__':
    print(strength_pwd("test"))  # 19
    print(strength_pwd("atest"))  # 33

    print(strength_pwd("abest"))  # 35
    print(strength_pwd("teest"))  # 28

    print(strength_pwd("teest"))  # 34
