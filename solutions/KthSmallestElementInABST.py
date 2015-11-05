__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *

class KthSmallestElementInABST(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{6,4,8,3,5,7}") ,4,),
            expects = 6
        )

    def solution(self, root, k):
        ret = self.inorder_traverse(root)
        return ret[k-1]

    def inorder_traverse(self,root):
        ret = []
        if root is None:
            return ret
        ret += self.inorder_traverse(root.left)
        ret += root.val,
        ret += self.inorder_traverse(root.right)
        return ret

    #in order traverse non-recurssion
    def solution(self, root, k):
        stack = []
        top = root
        while True:
            if top is not None:
                stack.append(top)
                top = top.left
            else:
                #access self
                top = stack.pop()
                k = k - 1
                if k == 0: return top.val
                #access right child
                top = top.right
        return -1