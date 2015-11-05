__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class PathSumII(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{5,4,8,11,#,13,4,7,2,#,#,5,1}"),22,),
            expects = [
                       [5,4,11,2],
                       [5,8,4,5]
                    ]
        )
        self.push_test(
            params = (TreeNode.deserialize("{5,4,8,11,#,13,4,7,2,#,#,5,1}"),222,),
            expects = []
        )

    def solution(self, root, sum):
        self.sum = sum

        # self.result = []
        # self.dfs_recurssive(root, [])
        # return self.result

        return list(self.dfs_yield(root, sum))

    def dfs_recurssive(self, root, path):
        if root is None:
            return
        if not root.left and not root.right:
            path += root.val,
            if sum(path) == self.sum:
                self.result+= path,
            else:
                return
        if root.left:
            self.dfs_recurssive(root.left, path[:] +  [root.val,] ),
        if root.right:
            self.dfs_recurssive(root.right, path[:] + [root.val,] ),

    def dfs_yield(self,root, total):
        if root is not None:
            if not root.left and not root.right and root.val == total:
                    yield [root.val,]
            else:
                for next in self.dfs_yield(root.left, total-root.val):
                    yield [root.val,] + next
                for next in self.dfs_yield(root.right, total -root.val):
                    yield [root.val,] + next