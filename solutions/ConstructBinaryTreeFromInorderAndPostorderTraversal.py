__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class ConstructBinaryTreeFromInorderAndPostorderTraversal(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([4,2,5,1,3,6],
                      [4,5,2,6,3,1]),
            expects = TreeNode.deserialize("{1,2,3,4,5,#,6}")
        )
    def solution(self, inorder, postorder):
        self.inorder = inorder
        self.postorder = postorder
        tree = self.buildTreeFromTraverse( 0, len(inorder), 0, len(postorder))
        return tree

    def buildTreeFromTraverse(self, istart, iend, pstart, pend):
        if istart == iend or pstart == pend: return None
        root = TreeNode( self.postorder[pend-1] )
        for split in xrange(istart, iend):
            if self.inorder[split] == self.postorder[pend -1]: break
        root.left = self.buildTreeFromTraverse(istart, split, pstart, pstart+split-istart)
        root.right = self.buildTreeFromTraverse(split+1, iend, pstart+split-istart, pend-1)
        return root