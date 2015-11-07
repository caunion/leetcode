from BaseSolution import *
from TreeNode import *

class LowestCommonAncestorOfABinaryTree(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        root = TreeNode.deserialize("[5,3,6,2,4,null,null,1]")
        self.push_test(
            params = (root, TreeNode(4), TreeNode(1)),
            expects = root.left
        )

    def solution(self, root, p, q):
        root.parent = None
        path1 = self.path2node(root, p)
        path2 = self.path2node(root, q)
        while path1:
            tmp = path1
            path1 = path1.parent
            tmp.parent = None
        while path2.parent:
            path2 = path2.parent
        return  path2

    def path2node(self, root, node):
        if not root:
            return None
        if root == node:
            return root
        else:
            ret = None
            if root.left:
                root.left.parent = root
                ret = self.path2node(root.left, node)
            if not ret and root.right:
                root.right.parent = root
                ret = self.path2node(root.right, node)
            return ret

    # Came to mind but fail to code
    # pay attention to this code!!
    def solution(self, root, p, q):
        if not root: return None
        if root == q or root== p :
            return root
        left = self.solution(root.left, p ,q)
        right = self.solution(root.right, p, q)
        if bool(left) != bool(right):
            return left or right
        if not left and not right:
            return None
        return root