__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *

class ValidateBinarySearchTree(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{1,2,3,#,#,4,#,#,5}") ,),
            expects = False
        )
        self.push_test(
            params = (TreeNode.deserialize("{6,4,8,3,5,7}"),),
            expects = True
        )
        self.push_test(
            params = (TreeNode.deserialize("{1,1}"),),
            expects = False
        )
        self.push_test(
            params = (TreeNode.deserialize("{2147483647}"),),
            expects = True
        )


    def solution(self, root):
        return self.dfs(root)

    def dfs(self, root, low = -float('Inf'), up=float('Inf')):
        ret = True
        if root is None:
            return ret
        else:
            ret = ret and low < root.val < up

        if not ret: return ret

        ret = ret and self.dfs(root.left, low, root.val)
        ret = ret and self.dfs(root.right, root.val, up)
        return ret