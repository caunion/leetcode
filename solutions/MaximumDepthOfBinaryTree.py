__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class MaximumDepthOfBinaryTree(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("[1,2]"),),
            expects = 2
        )
        self.push_test(
            params = (TreeNode.deserialize("[1,2,3,null,4,5,6,7]"),),
            expects = 4
        )
    def solution(self, root):
        return self.dfs_recurssive(root)

    def dfs_recurssive(self, root):
        if root is None:
            return 0
        ld = self.dfs_recurssive(root.left)
        rd = self.dfs_recurssive(root.right)
        return max(ld + 1, rd + 1)