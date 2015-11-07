__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class LowestCommonAncestorOfABinarySearchTree(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        root = TreeNode.deserialize("[5,3,6,2,4,null,null,1]")
        self.push_test(
            params = (root, TreeNode(4), TreeNode(1)),
            expects = root.left
        )

    def solution(self, root, p, q):
        if not p or not q: return p or q
        if p == q: return p
        if p.val > q.val: p, q = q, p
        return self.lca(root, p, q)

    def lca(self, root, p, q):
        if not root: return None
        if root.val < p.val:
            root = self.lca(root.right, p, q)
        if root.val > q.val:
            root= self.lca(root.left,p, q)
        return root
