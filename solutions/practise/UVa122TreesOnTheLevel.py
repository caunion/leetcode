__author__ = 'Daoyuan'
from ..BaseSolution import *

class Node:

    def __init__(self, val):
        self.__init__(self)
        self.val = val

    def __init__(self):
        self.left = None
        self.right = None
        self.val = -1

class UVa122TreesOnTheLevel(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([
                "(11,LL) (7,LLL) (8,R) (5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()",
                "(3,L) (4,R) ()"
                      ],),
            expects = [
                "5 4 8 11 13 4 7 2 1",
                "-1"
                ]
            )
    def solution(self, params):
        result = []
        for line in params:
            ret = []
            segs = line.strip().split(' ')
            vals  = []
            paths = []
            for seg in segs:
                seg = seg.strip(")").strip("(")
                if seg == "": break
                ss = seg.split(",")
                vals.append(  int(ss[0]) )
                paths.append( ss[1] )

            I = sorted(range(0, len(paths)), key = lambda i : paths[i])
            root = Node()
            for i in I:
                val = vals[i]
                path = paths[i]
                tmp = root
                if path == "":
                    tmp.val = val
                else:
                    for c in path:
                        if c=="L":
                            if tmp.left is None:
                                tmp.left = Node()
                            tmp = tmp.left
                        else:
                            if tmp.right is None:
                                tmp.right = Node()
                            tmp = tmp.right
                    tmp.val = val

            ret = self.layerwise_traverse(root)
            agg=" ".join([str(i) for i in ret])
            if -1 in ret:
                agg = "-1"
            result.append(agg)
        return result

    def layerwise_traverse(self, node):
        stack = [node]
        ret = []
        while len(stack) > 0:
            top = stack.pop(0)
            ret.append(top.val)
            if top.left is not None:
                stack.append(top.left)
            if top.right is not None:
                stack.append(top.right)
        return ret
