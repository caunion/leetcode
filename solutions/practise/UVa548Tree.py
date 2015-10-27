__author__ = 'Daoyuan'

from ..BaseSolution import *

class Node:

    # def __init__(self, val):
    #     self.val = val

    def __init__(self):
        self.val = -1
        self.left = None
        self.right = None


class UVa548Tree(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([
                "3 2 1 4 5 7 6",
                "3 1 2 5 6 7 4",
                "7 8 11 3 5 16 12 18",
                "8 3 11 7 16 18 12 5",
                "255",
                "255"
            ],),
            expects = [1,3,255]
        )

    def solution(self, params):
        result = []
        for i in xrange(len(params)/2):
            in_order = params[i*2]
            post_order = params[i*2 + 1]
            in_order = [ int(i) for i in in_order.split(' ')]
            post_order = [int(i) for i in post_order.split(' ')]
            root = self.reconstruct_tree( in_order, post_order)
            ret = self.min_weight(root)
            result.append(ret[0].val)
        return result
    
    def min_weight(self, root):
        if root is None:
            return  -1
        left = self.min_weight(root.left)
        right = self.min_weight(root.right)
        if left == -1 and right == -1: return [root]
        elif left == -1:
            right.append(root)
            return right
        elif right == -1:
            left.append(root)
            return left
        else:
            if right[-1].val < left[-1].val:
                right.append(root)
                return right
            else:
                left.append(root)
                return left

    def reconstruct_tree(self, in_order, post_order):
        length = len(in_order)
        root = Node()
        root.val = post_order[-1]
        leftlen = 0
        for i in in_order:
            if i == post_order[-1]: break
            leftlen = leftlen + 1
        rightlen = length - leftlen - 1

        if leftlen > 0:
            root.left = self.reconstruct_tree(in_order[0:leftlen], post_order[0:leftlen])
        if rightlen > 0:
            root.right = self.reconstruct_tree(in_order[ 1 + leftlen : length], post_order[leftlen : length-1])

        return root