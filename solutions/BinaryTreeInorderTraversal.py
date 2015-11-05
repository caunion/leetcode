__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class BinaryTreeInorderTraversal(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{1,#,2,3}"),),
            expects = [1,3,2]
        )

    def solution(self, root):
        return self.inorder_interative(root)

    def inorder_traverse(self,root):
        if root is None:
            return []
        ret = []
        ret += self.inorder_traverse(root.left)
        ret += root.val,
        ret += self.inorder_traverse(root.right)
        return ret

    def inorder_interative(self,root):
        if root is None: return []
        ret =[]
        stack = [ (root, 0) ]
        top, state = None, None
        while True:
            if top is None:
                if len(stack)==0: break
                top, state = stack.pop()
                continue
            if state == 0:
                stack += (top, 1),
                top, state = top.left, 0
            elif state == 1:
                ret.append( top.val )
                state = 2
            else:
                top, state = top.right, 0
        return ret