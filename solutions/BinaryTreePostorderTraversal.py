__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class BinaryTreePostorderTraversal(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{1,#,2,3}"),),
            expects = [3,2,1]
        )
        self.push_test(
            params = (TreeNode.deserialize("{1}"),),
            expects = [1]
        )
        self.push_test(
            params = (TreeNode.deserialize("{1,2,3,#,4,5,#,#,6,#,7}"),),
            expects = [6,4,2,7,5,3,1]
        )
    def solution(self, root):
        return self.postorder_iterative2(root)

    def postorder_traverse(self,root):
        ret = []
        if root is None:
            return ret
        ret += self.postorder_traverse(root.left)
        ret += self.postorder_traverse(root.right)
        ret += root.val,
        return ret

    def postorder_iterative(self,root):
        if root is None: return []
        stack = [root]
        ret = []
        top = None
        while True:
            if top is None:
                top = stack.pop()
                continue
            if not hasattr(top,'leftFlag'):
                stack.append(top)
                top.leftFlag = True
                top = top.left
            elif not hasattr(top,'rightFlag'):
                stack.append(top)
                top.rightFlag = True
                top = top.right
            else:
                ret.append(top.val)
                if len(stack) == 0: break
                top = stack.pop()
        return ret

    def postorder_iterative2(self, root):
        if root is None: return []
        stack = [(root, 0)]
        ret = []
        top = None; state = None
        while True:
            if top is None:
                top, state = stack.pop()
                continue
            if state == 0:
                stack.append( (top, 1) )
                top = top.left
                state = 0
            elif state == 1:
                stack.append( (top, 2))
                top = top.right
                state = 0
            else:
                ret.append( top.val)
                if len(stack) == 0:
                    break
                top, state = stack.pop()
        return ret
