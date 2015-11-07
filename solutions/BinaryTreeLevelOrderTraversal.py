from BaseSolution import *
from TreeNode import *
class BinaryTreeLevelOrderTraversal(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, root):
        result, level = [], [root]
        while len(level) > 0:
            result.append( [ node.val for node in level])
            level = [ node for n in level for node in (n.left, n.right) if node]
        return result