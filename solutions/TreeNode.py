__author__ = 'Daoyuan'

class TreeNode(object):
    def __init__(self, val= -1, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def serialize(self):
        queue = [ self ]
        idx = 0
        ret = []
        while len(queue) > 0:
            top = queue.pop(0)
            ret.append(str(top.val))
            if top.left is not None:
                queue.append(top.left)
            if top.right is not None:
                queue.append(top.right)
        return "{" +",".join(ret) +"}"

    @staticmethod
    def deserialize(treestr):
        if len(treestr) == 0 or treestr=="{}":
            return TreeNode()
        if treestr[0] == "{" or treestr[0] =="[":
            treestr= treestr[1:-1]
        arr = treestr.split(",")
        root = TreeNode.bfs(arr)
        return root
    @staticmethod
    def bfs(arr):
        if len(arr) == 0 : return TreeNode()
        root = TreeNode( int(arr[0]) )
        queue = [root]
        i = 1
        while queue.__len__() > 0:
            if i >= len(arr): break
            top = queue.pop(0)
            if arr[i] != "#" and arr[i]!="null":
                top.left = TreeNode( int(arr[i]))
                queue.append(top.left)
            i = i + 1
            if i >= len(arr): break
            if arr[i] != "#" and arr[i] != "null":
                top.right = TreeNode(int(arr[i]))
                queue.append(top.right)
            i = i + 1
        return root

    #def treelikestr(self):