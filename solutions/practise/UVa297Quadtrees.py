__author__ = 'Daoyuan'

from ..BaseSolution import *

class quadNode():
    def __init__(self, c=-1):
        self.color = c
        self.first = None
        self.second = None
        self.third = None
        self.forth = None

class UVa297Quadtrees(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([
                "3",
                "ppeeefpffeefe",
                "pefepeefe",
                "peeef",
                "peefe",
                "peeef",
                "peepefefe"
                      ],),
            expects = [640, 512, 384]
        )

    def solution(self, params):
        n = int(params[0])
        result = []
        for i in xrange(n):
            pixel = 1024
            left = params[i*2 + 1]
            right = params[i*2 + 2]
            left = [self.color2num(c) for c in left]
            right =[self.color2num(c) for c in right]
            leftTree = self.build(left, [0])
            rightTree = self.build(right, [0])
            ret = self.draw(leftTree, rightTree, pixel)
            result.append(ret)
        return result
    def draw(self, left, right, pixel):
        if left == None and right.color == 2:
            return pixel
        if left == None and right.color == 0:
            return 0
        if right == None and left.color == 2:
            return pixel
        if right == None and left.color == 0:
            return 0
        if left.color == 2 or right.color == 2:
            return pixel
        if left.color == 0 and right.color == 0:
            return 0
        black = 0
        black = black + self.draw(left.first, right.first, pixel / 4)
        black = black + self.draw(left.second, right.second, pixel /4)
        black = black + self.draw(left.third, right.third, pixel/4)
        black = black + self.draw(left.forth, right.forth, pixel/4)
        return black

    def color2num(self, c):
        if c == "p": return 1
        if c == "e": return 0
        if c == "f": return 2

    def build(self, raw, idx):
        cur = idx[0]
        rootc = raw[cur]
        root = quadNode(raw[cur])
        if rootc == 1: #there must be child
            idx[0] = idx[0] + 1
            root.first = self.build(raw, idx)
            idx[0] = idx[0] + 1
            root.second = self.build(raw,idx)
            idx[0] = idx[0] + 1
            root.third = self.build(raw, idx)
            idx[0] = idx[0] + 1
            root.forth = self.build(raw, idx)
        return root