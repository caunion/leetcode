__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class UniqueBinarySearchTreesII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 8
        self.push_test(
            params = (3,),
            expects = [
                TreeNode.deserialize("{1,#,3,2}"),
                TreeNode.deserialize("{3,2,#,1}"),
                TreeNode.deserialize("{3,1,#,#,2}"),
                TreeNode.deserialize("{2,1,3}"),
                TreeNode.deserialize("{1,#,2,#,3}")
            ],
            expect_unordered= True
        )

    # by myself
    def solution(self, n):
        if not hasattr(self, 'trees'):
            self.trees = [ [None], [TreeNode(1)]]
        self.solve(n)
        return self.trees[n]

    def solve(self, n):
        if n < len(self.trees):
            return self.trees[n]
        result = []
        for left in xrange(0,n):
            right = n - 1 -left
            for leftnode in self.solve(left):
                for rightnode in self.solve(right):
                    root = TreeNode(left+1)
                    offset = left + 1
                    rightnode = self.fixAndCopyRightTree(rightnode, offset)
                    root.left = leftnode
                    root.right = rightnode
                    result.append(root)
        self.trees.append(result)
        return self.trees[n]

    def fixAndCopyRightTree(self, root, offset):
        if not root: return None
        newroot = TreeNode(root.val + offset)
        newroot.left = self.fixAndCopyRightTree(root.left, offset)
        newroot.right = self.fixAndCopyRightTree(root.right, offset)
        return newroot