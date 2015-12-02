__author__ = 'Daoyuan'
from ..BaseSolution import *
from ..TreeNode import *

class C22_2_8_TreeDiameter(BaseSolution):

    """
    22.2-8, page 602, tree diameter
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{1,2,3,4,5,6,#,#,#,7,#,#,8,#,#,9,#,#,10}"),),
            expects = 8
        )
        self.push_test(
            params = (TreeNode.deserialize("{1,2,3,4,5,6,#,#,#,7,#,#,8,#,#,9,11,#,10}"),),
            expects = 8
        )
        self.push_test(
            params = (TreeNode.deserialize("{1,#,3}"),),
            expects = 1
        )
        self.push_test(
            params = (TreeNode.deserialize("{1}"),),
            expects = 0
        )
        self.push_test(
            params = (None,),
            expects = 0
        )
    def bfs(self, root):
        queue = [root]
        height = 0
        child = None
        while len(queue) > 0:
            top = queue.pop(0)
            if not top: continue
            if not child:
                child = top.left or top.right
            if child and top.equals(child):
                height+=1
                child = top.left or top.right
            for sub in (top.left, top.right):
                if not sub: continue
                sub.parent = top
                queue.append(sub)

        return height, top

    def reverse(self, last):
        cur = last
        assign = 0
        prev = None
        while cur:
            parent = cur.parent
            cur.parent = prev
            if assign == 0:
                cur.left = parent
            else:
                cur.right = parent
            if not parent:
                break
            if parent.left and parent.left.equals(cur):
                assign = 0
            else:
                assign = 1
            prev = cur
            cur = parent
        return last
    def recursive_reverse(self, root, prev):
        if not root: return
        if root.left and root.left.equals( prev ):
            root.left = root.parent
        else:
            root.right = root.parent
        parent = root.parent
        root.parent  = prev
        self.recursive_reverse(parent, root)

    def solution(self, root):
        if not root: return 0
        h1, last =  self.bfs(root)
        self.recursive_reverse(last, None)
        h2, last = self.bfs(last)
        return h2
