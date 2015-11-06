__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *

class TreeLinkNode(TreeNode):
    def __init__(self, val=-1, left = None, right=None, next = None):
        TreeNode.__init__(val, left,right)
        self.next = next

class PopulatingNextRightPointersInEachNode(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("[0]"),)
        )
        self.push_test(
            params = (TreeNode.deserialize("1,2,3,4,5,6,7"),)
        )
    def solution(self, root):
        self.bfs(root)
        return root

    def bfs(self, root):
        if not root: return root
        queue = [root]
        prev = None
        count = 0
        layer = [2**i for i in range(1,20)]
        while len(queue) > 0:
            count = count + 1
            top = queue.pop(0)
            top.next = None
            if prev and count not in layer:
                prev.next = top
            elif prev:
                prev.next = None
            if top.left: queue.append(top.left)
            if top.right: queue.append(top.right)
            prev = top
        return root