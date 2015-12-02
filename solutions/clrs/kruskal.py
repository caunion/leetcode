__author__ = 'Daoyuan'
from ..BaseSolution import *
from ..GraphNode import *
from ..TreeNode import *
from DisjointSet import *

class Kruskal(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (Graph.deserialize( "{0,1@1,2@2#1,2@3#2#3,1@4,4@5#4,2@6}", True, True), ),
        )
    def solution(self, G):
        edges = []
        for node in G.V.values():
            for next,weight in node.neighbors:
                if next.x > node.x:
                    edge = [node.x, next.x, weight]
                else:
                    edge = [next.x, node.x, weight]
                edges.append(edge)
        edges = sorted(edges, cmp = lambda x,y : (x[0] - y[0]) * 100 + (x[1]-y[1])*10 + int(x[2] - y[2]))
        cleared = [edges[0]]
        prev = edges[0]
        for edge in edges:
            if prev == edge:
                continue
            else:
                prev = edge
                cleared.append(edge)

        dset = DisjointSet()
        for node in G.V.values():
            dset.makeset(node.x)

        edges = sorted(cleared, key= lambda x:x[2])
        tree = []
        for edge in edges:
            u, v, weight = edge
            if not dset.findset(u).equals( dset.findset(v) ):
                dset.union(u,v)
                tree.append( edge )
        return tree

