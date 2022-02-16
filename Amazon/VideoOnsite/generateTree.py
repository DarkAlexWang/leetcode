"""
How to use:

root = generateTree(generateNodesFromX(generateCharSetX(), 20, 40))
res = []
getTree(root, res)
print res
"""
import random
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generateCharSetX():
    return [x for x in range(1000)]

def generateNodesFromX(x, min_elements, max_elements):
    num_nodes = random.randrange(min_elements, max_elements)
    set_nodes = set([])
    while len(set_nodes) < num_nodes:
        set_nodes.add(x[random.randrange(0, len(x))])
    return set_nodes
#Data structure involved functions
def getTree(root, s):
    if root == None and len(s) > 0:
        s.append('null')
        return
    s.append(root.val)
    getTree(root.left, s)
    getTree(root.right, s)

def generateTree(s):
    val = s.pop()
    root = TreeNode(val)
    while len(s) > 0:
        val = s.pop()
        curr = root
        while 1:
            if curr.val > val and curr.left == None:
                curr.left = TreeNode(val)
                break
            elif curr.val < val and curr.right == None:
                curr.right = TreeNode(val)
                break
            if curr.val > val:
                curr = curr.left
            elif curr.val < val:
                curr = curr.right
    return root
