#
# @lc app=leetcode id=358 lang=python3
#
# [358] Rearrange String k Distance Apart
#

# @lc code=start
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not s:
            return ''
        count = collections.defaultdict(int)
        for w in s:
            count[w] += 1

        # sort the letters according to the frequency
        stack = sorted(list(count.items()), key=lambda t : t[1])

        # get most frequent character
        char, count = stack.pop()
        lst = [[char] for _ in range(count)]

        # take care of the letters with same highest freq
        while stack and stack[-1][1] == count:
            char, _ = stack.pop()
            for l in lst:
                l.append(char)

        # all the character left
        res = ''.join(c * n for c, n in stack)

        #padding
        for i, r in enumerate(res):
            lst[i % (len(lst) - 1)].append(r)

        for l in lst[:-1]:
            if len(l) < k:
                return ''

        return ''.join(''.join(l) for l in lst)


# @lc code=end
