__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class BinaryTreePaths(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{1,2,3,#,5}"),),
            expects = ["1->2->5","1->3"]
        )
        self.push_test(
            params = (TreeNode.deserialize("{1}"),),
            expects = ["1"]
        )
        self.push_test(
            params = (None,),
            expects = []
        )
    def solution(self,root):
        ret = list(self.dfs_yield(root))
        return ["->".join(item) for item in ret]

    def dfs_yield(self, root):
        if root is None:
            return
        if not root.left and not root.right:
            yield [ str(root.val),]
        else:
            for next in self.dfs_yield(root.left):
                yield [str(root.val),] + next
            for next in self.dfs_yield(root.right):
                yield [str(root.val),] + next