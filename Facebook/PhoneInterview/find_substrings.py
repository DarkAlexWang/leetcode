from collections import Counter
from typing import List


# Go fwd till exhausting 1 letter: ctr[ch] == ctr_glob[ch].  Then bwd in the found stretch to try to
# extract the  substring
def find_substrings(s: str) -> List[str]:
    """ O(26*N) """
    # similar to LC partition-label
    def getsub(i,prev):
        ctr = Counter()
        for k in range(i,prev-1,-1):
            ctr[s[k]] += 1
            if ctr[s[k]] == ctr_glob[s[k]]:
                del ctr[s[k]]
            if len(ctr) == 0:
                return s[k:i+1]
        return ''

    ans = []
    ctr_glob = Counter(s)
    ctr = Counter()
    prev = 0
    for i,ch in enumerate(s):
        ctr[ch] += 1
        if ctr[ch] == ctr_glob[ch]:
            lft = getsub(i,prev)
            if lft:
                ans.append(lft)
                ctr = Counter()
                prev = i+1
    return ans


if __name__ == '__main__':
    print(find_substrings("baddacxb"))        # ['dd', 'c', 'x']
    print(find_substrings("badadcxb"))      # ['adad', 'c', 'x']
    print(find_substrings("babab"))           # ['babab']
    print(find_substrings("bcbaacb"))        # ['aa']
    print(find_substrings("bacadaeab"))      # ['c', 'd', 'e']
    print(find_substrings("bacadecbedb"))  # ['acadeced']
