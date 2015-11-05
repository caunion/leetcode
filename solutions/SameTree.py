__author__ = 'Daoyuan'
from BaseSolution import  *
from TreeNode import *
class SameTree(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, p, q):
        return self.serialize(p) == self.serialize(q)

    def serialize(self, root):
        ret = []
        queue = [root]
        while len(queue) > 0:
            top= queue.pop(0)
            if top is None:
                ret += ['#',]
                continue
            else:
                ret += [str(top.val),]
            queue.append(top.left)
            queue.append(top.right)
        return "{"+ ",".join(ret) + "}"