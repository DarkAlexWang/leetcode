Zhihuan Wang

=== level order ====
        [1]
     /       \
[2]           [3]
   \            /
    [5]        [4]

==> 1,2,3,4

class TreeNode:
    def __init__(val):

        node.val = val
        node.left = None
        node.right = None
class Solution:
    def level_order_tranversal(self, root):
        if not root:
            return None
        res = []
        q = collections.deque(root)
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res

====Recover string ====
String "javaisgood"
        "javadisgood"

    output:
            1
set["Java", "i", "d", "javad", "is", "good", "or"]
==> "java is good"

"is good java"
word = java is dic
res.append(word + ' ')

class solution:
    def recover_string(self, s, dic):
        if not s:
            return ""
        res = ''
        word = ''
        s_list = list(s) # ['j', 'a', 'v'] //
        n = len(s)
        for i in s_list:
            word += s[i]
            if word is in dic:
                res += word
                if i != n -1:
                    res += ' '
                    word = ''
            else:
                continue
        return res

s = o
word = 'is'

res = 'java is '

pointer = 9
