__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class SymmetricTree(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{2,3}"),),
            expects = False
        )
        self.push_test(
            params = (TreeNode.deserialize("{2,3,3,4,#,#,4,#,5,5,#,#,6,6,#,7,8,8,7,9,0,0,1,1,0,0,9}"),),
            expects = True
        )
        self.push_test(
            params = (TreeNode.deserialize("{1,2,2,3,4,4,3}"), ),
            expects =  True
        )
        self.push_test(
            params = (TreeNode.deserialize("{1,2,3,#,#,4,#,#,5}"), ),
            expects =  False
        )
        self.push_test(
            params = (TreeNode.deserialize("{1,2,2,3,4,4,3,#,#,5,#,#,5}"), ),
            expects =  True
        )

    def solution(self, root):
        if root is None or \
                root.left is None and root.right is None:
            return True
        if root.left is not None and root.right is not None:
            left = self.serialize(root.left)
            right = self.serialize( self.dfs(root.right) )
            return left == right
        return False

    def serialize(self, root):
        queue = [ root ]
        idx = 0
        ret = []
        while len(queue) > 0:
            top = queue.pop(0)
            if top is None:
                ret+="#"
                continue
            else: ret.append(str(top.val))
            queue.append(top.left)
            queue.append(top.right)
        return "{" +",".join(ret) +"}"

    def dfs(self, root):
        if root is not None:
            root.left, root.right = root.right, root.left
            self.dfs(root.left)
            self.dfs(root.right)

        return root
    def bfs(self, root):
        queue = [ root ]
        dep = 0
        levelbuf = []
        while len(queue) > 0:
            top = queue.pop(0)
            if top is None: continue
            if len(queue)==0 or top.dep != dep:
                if levelbuf != levelbuf[::-1]:
                    return False
                dep = top.dep
                levelbuf = []
            levelbuf += str(top.val)
            queue.append(top.left)
            queue.append(top.right)
        return True