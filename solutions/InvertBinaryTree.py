from BaseSolution import *
from TreeNode import *
class InvertBinaryTree(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("[4,2,7,1,3,6,9]"),),
            expects = TreeNode.deserialize("[4,7,2,9,6,3,1]")
        )
    def solution(self, root):
        self.myInvertTree(root)
        return root

    def myInvertTree(self, root):
        if not root: return
        root.left, root.right = root.right, root.left
        self.myInvertTree(root.left)
        self.myInvertTree(root.right)
        return

