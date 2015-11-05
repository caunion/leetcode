__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class SumRootToLeafNumbers(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{1,2,3}"),),
            expects = 25
        )
        self.push_test(
            params = (TreeNode.deserialize("{4,9,0,#,1}"),),
            expects = 531
        )
    def solution(self, root):
        return  self.dfs_recursive(root,0)

    def dfs_recursive(self, root, sum):
        ret = 0
        if root is None: return 0
        if not root.left and not root.right: return sum+root.val
        sum = (sum+root.val) * 10
        if root.left is not None:
            ret += self.dfs_recursive(root.left, sum)
        if root.right is not None:
            ret += self.dfs_recursive(root.right, sum)
        return ret

    def dfs_iterative(self,root):
        if root is None: return 0
        stack = [ (root, 0, 0) ]
        top, state, total = None, None, None
        ret = []
        while True:
            if top is None:
                if len(stack) == 0: break
                top, state, total = stack.pop()
                continue
            if state == 0:
                total += top.val
                state = 1
                if top.left is None and top.right is None:
                    ret += total, # save leave value to ret
            elif state == 1:
                stack += (top, 2, total),
                top, state, total = top.left, 0, total*10
            else:
                top, state, total = top.right, 0, total*10

        return sum(ret)