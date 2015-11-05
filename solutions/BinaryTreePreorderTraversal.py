__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *

class BinaryTreePreorderTraversal(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{1,#,2,3}"),),
            expects = [1,2,3]
        )

    def solution(self, root):
        return self.preorder_iterative(root)

    def preorder_traverse(self,root):
        ret = []
        if root is None:
            return ret
        ret += root.val,
        ret += self.preorder_traverse(root.left)
        ret += self.preorder_traverse(root.right)
        return ret
    def preorder_iterative(self,root):
        if root is None: return []
        ret =[]
        stack = [ (root,0) ]
        top, state = None, None
        while True:
            if top is None:
                if len(stack) == 0: break
                top, state = stack.pop()
                continue
            if state == 0:
                ret += top.val,
                state = 1
            elif state== 1:
                stack += (top, 2),
                top, state = top.left, 0
            else:
                top, state = top.right, 0
        return ret

