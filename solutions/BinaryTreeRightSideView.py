__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *

class BinaryTreeRightSideView(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{1,2,3,#,5,#,4}"),),
            expects = [1,3,4]
        )
        self.push_test(
            params = (TreeNode.deserialize("[1,2,3,4,5,6,#,7]"),),
            expects = [1,3,6,7]
        )
    def solution(self, root):
        return self.bfs(root)

    def bfs(self,root):
        if not root: return []
        ret = []
        queue = [root]
        prev = TreeNode()
        nextfirst = root.left or root.right
        while queue:
            top = queue.pop(0)
            if top == nextfirst:
                ret.append(prev.val)
                nextfirst = None
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
            if not nextfirst:
                nextfirst = top.left or top.right
            prev = top
        ret.append(top.val)
        return ret

