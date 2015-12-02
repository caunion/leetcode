__author__ = 'Daoyuan'
from ..BaseSolution import *
from ..TreeNode import *


class DisjointSet():
    def __init__(self):
        self.trees = {}
        pass
    def makeset(self, element):
        node = TreeNode(element)
        node.parent = node
        node.rank = 1
        self.trees[element] = node
        return node

    def findset(self, element):
         node = self.trees[element]
         while not node.equals(node.parent):
            node = node.parent
         return node

    def union(self, u, v):
        rootu = self.findset(u)
        rootv = self.findset(v)
        if rootu.rank >= rootv.rank:
            rootv.parent = rootu
            rootu.rank += rootv.rank
        else:
            rootu.parent = rootv
            rootv.rank += rootu.rank

class DisjointSetTest(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,2,3,4,5,6,7,8,9,10],[[1,3],[2,4],[10,1],[5,6],[8,9],[9,10]],),
            expects = [1,2,1,2,5,5,7,1,1,1]
        )
        self.push_test(
            params = ([1,2,3,4,5,6,7,8,9,10],[[1,3],[2,4],[10,1],[5,6],[8,9],[9,10],[7,5],[4,9]],),
            expects = [1,1,1,1,5,5,5,1,1,1]
        )
    def solution(self, elements, unions):
        dset = DisjointSet()
        for e in elements: dset.makeset(e)
        for pair in unions: dset.union( *pair)
        ret = []
        for e in elements:
            ret.append(dset.findset(e).val)
        return ret