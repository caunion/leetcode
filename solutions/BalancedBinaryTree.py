__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class BalancedBinaryTree(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, root):
        self.flag = True
        self.dfs_recurssive(root)
        return self.flag

    def dfs_recurssive(self, root):
        if not self.flag: return -1
        if root is None: return 0
        ld = self.dfs_recurssive(root.left)
        rd = self.dfs_recurssive(root.right)
        if abs(rd - ld) > 1:
            self.flag = False
        return max(rd+1, ld+1)