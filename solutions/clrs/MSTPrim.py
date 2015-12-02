__author__ = 'Daoyuan'
from ..BaseSolution import *
from ..TreeNode import *
from ..GraphNode import *

class MSTPrim(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (Graph.deserialize( "{0,1@1,2@2#1,2@3#2#3,1@4,4@5#4,2@6}", True, True), ),
        )
    def solution(self, G):
        return self.prim(G,G.V.values()[0])

    def prim(self, G, r):
        for node in G.V.values():
            node.key = int( (1 << 31) - 1)
            node.p = None
        heap = G.V.values()
        r.key = 0
        while len(heap) > 0:
            u = self.get_min(heap)
            for next,weight in u.neighbors:
                if heap.__contains__(next) and weight < next.key:
                    next.key = weight
                    next.p = u
        ret = []
        while u:
            ret.append( u.x )
            u = u.p
        ret.reverse()
        return ret

    def get_min(self,heap):
        minkey = min( [item.key for item in heap])
        ret = filter( lambda x: x.key == minkey, heap)[0]
        heap.remove(ret)
        return ret