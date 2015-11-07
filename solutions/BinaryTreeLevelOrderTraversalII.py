from BaseSolution import *
from TreeNode import *
class BinaryTreeLevelOrderTraversalII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, root):
        result, level = [], [root]
        while root and len(level) > 0:
            result.insert(0, [node.val for node in level])
            level = [node for n in level for node in (n.left, n.right) if node]
        return result