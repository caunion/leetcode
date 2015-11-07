__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class FlattenBinaryTreeToLinkedList(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params=(TreeNode.deserialize("[1,2,null,3]"),),
            expects = "{1,#,2,#,3}"
        )
    def solution(self, root):
        if root:
            self.dfs_inplace(root)
        return root.serialize()

    def dfs_inplace(self, root):
        if not root.left and not root.right:
            return (root, root)
        lh = le = rh = re= None
        if root.left:
            lh, le = self.dfs_inplace(root.left)
            root.left = None
        if root.right:
            rh, re = self.dfs_inplace(root.right)
        head = root
        if lh:
            head.right = lh
            head = le
            head.left = head.right = None
        if rh:
            head.right = rh
            head = re
            head.left = head.right = None
        return (root, head)


