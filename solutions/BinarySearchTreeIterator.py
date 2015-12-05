__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *

class BSTIterator(object):
    stack = []
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushAll(root)
    def pushAll(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            top = self.stack.pop()
            self.pushAll(top.right)
            return top.val
        else:
            return -1<<30

class BinarySearchTreeIterator(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{5,3,7,1,4,6,9,#,2,#,#,#,#,8,10}"), 10),
            expects = range(1,11)
        )
    def solution(self, root, n):
        itr = BSTIterator(root)
        ret = []
        for i in xrange(n):
            ret.append(itr.next())
        return ret