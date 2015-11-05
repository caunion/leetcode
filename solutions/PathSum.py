__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class PathSum(BaseSolution):

    """
    Three way of DFS: recursive, iterative and yield-style
    yield: top-down
    recursive: bottom-up
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 8
        self.push_test(
            params = (TreeNode.deserialize("{5,4,8,11,#,13,4,7,2,#,#,#,1}"),22,),
            expects = True
        )
        self.push_test(
            params = (TreeNode.deserialize("{5,4,8,11,#,13,4,7,2,#,#,#,1}"),232,),
            expects = False
        )
        self.push_test(
            params = (TreeNode.deserialize("{}"),0,),
            expects = False
        )


    def solution(self, root, sum):
        self.sum = sum
        #return self.dfs_iterative(root)
        # ret = list(self.dfs_yield(root))
        # return sum in ret
        return self.dfs_recursive(root,0)
    def dfs_recursive(self,root, total):
        ret = False
        if root is None: return False
        tmp = total + root.val
        if root.left is None and root.right is None:
            if tmp == self.sum: return True
            else: return False
        if root.left:
            ret = ret or self.dfs_recursive(root.left, tmp)
        if root.right:
            ret = ret or self.dfs_recursive(root.right,tmp)
        return ret

    def dfs_iterative(self,root):
        ret = False
        if root is None: return ret
        stack = [ (root, 0, 0)]
        top, state, total = None, None, 0
        while not ret:
            if top is None:
                if len(stack) == 0: break
                top, state, total = stack.pop()
                continue
            if state == 0:
                total += top.val
                state = 1
                if not top.left and not top.right and total ==  self.sum:
                    ret = True
            elif state == 1:
                stack += (top, 2, total),
                top, state, total = top.left, 0, total
            else:
                top, state, total = top.right, 0, total
        return ret

    def dfs_yield(self,root):
        if root is None:
            yield -1e9
            return
        if not root.left and not root.right:
            yield root.val
        else:
            for next in self.dfs_yield(root.left):
                yield root.val + next
            for next in self.dfs_yield(root.right):
                yield root.val + next