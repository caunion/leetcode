__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *

class TreeLinkNode(TreeNode):
    def __init__(self, val=-1, left = None, right=None, next = None):
        TreeNode.__init__(self,val, left,right)
        self.next = next
    @staticmethod
    def deserialize(treestr):
        if len(treestr) == 0 or treestr=="{}":
            return TreeLinkNode()
        if treestr[0] == "{" or treestr[0] =="[":
            treestr= treestr[1:-1]
        arr = treestr.split(",")
        root = TreeLinkNode.bfs(arr)
        return root
    @staticmethod
    def bfs(arr):
        if len(arr) == 0 or arr[0] == "" : return None
        root = TreeLinkNode( int(arr[0]) )
        queue = [root]
        i = 1
        while queue.__len__() > 0:
            if i >= len(arr): break
            top = queue.pop(0)
            if arr[i] != "#" and arr[i]!="null":
                top.left = TreeLinkNode( int(arr[i]))
                queue.append(top.left)
            i = i + 1
            if i >= len(arr): break
            if arr[i] != "#" and arr[i] != "null":
                top.right = TreeLinkNode(int(arr[i]))
                queue.append(top.right)
            i = i + 1
        return root

class PopulatingNextRightPointersInEachNodeII(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 8
        # self.push_test(
        #     params = (TreeLinkNode.deserialize("[0]"),)
        # )
        self.push_test(
            params = (TreeLinkNode.deserialize("1,2,3,4,5,#,7"),)
        )
    def solution(self, root):
        self.bfs(root)
        return root

    def bfs(self, root):
        head = child = TreeLinkNode(0)
        while root:
            child.next = root.left
            if child.next: child =child.next
            child.next = root.right
            if child.next: child = child.next
            if root.next: 
                root = root.next
            else:
                root = head.next
                head = child = TreeLinkNode(0)
