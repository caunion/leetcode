__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class MinimumDepthOfBinaryTree(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("[1,2]"),),
            expects = 2
        )
        self.push_test(
            params = (TreeNode.deserialize("[1,2,3,null,4,5,6,7,8,9]"),),
            expects = 3
        )
    def solution(self,root):
        return self.dfs_recurssive(root)


    def dfs_recurssive(self,root):
        if root is None or not root.left and not root.right:
            return 1
        ld = rd = 1e9
        if root.left: ld = self.dfs_recurssive(root.left)
        if root.right: rd = self.dfs_recurssive(root.right)
        ret = min ( 1+ld, 1+rd)
        if ret >= 1e8: return 1
        else: return ret

    def dfs_recurssive(self, root):
        if root is None:
            return 0
        ld = self.dfs_recurssive(root.left)
        rd = self.dfs_recurssive(root.right)
        if ld == 0:
            return rd+1
        if rd == 0:
            return ld + 1
        return min(ld + 1, rd + 1)
