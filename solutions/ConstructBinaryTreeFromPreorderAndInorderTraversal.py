__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *

class ConstructBinaryTreeFromPreorderAndInorderTraversal(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (
                [1,2,4,5,3,6],
                [4,2,5,1,3,6],),
            expects = TreeNode.deserialize("{1,2,3,4,5,#,6}")
        )

    def solution(self, preorder, inorder):
        plen, ilen= len(preorder), len(inorder)
        tree= self.buildTreeFromTraverse(preorder,0, plen, inorder, 0, ilen)
        return tree
    def buildTreeFromTraverse(self, preorder, pstart, pend, inorder, istart, iend):
        if istart == iend or pstart == pend: return None
        root = TreeNode(preorder[pstart])
        for rootidx in xrange(istart, iend):
            if preorder[pstart] == inorder[rootidx]:
                break
        root.left = self.buildTreeFromTraverse(preorder, pstart+1, pstart+1+rootidx-istart, inorder, istart, rootidx)
        root.right = self.buildTreeFromTraverse(preorder, pstart+1+rootidx-istart, pend, inorder, rootidx+1, iend)
        return root