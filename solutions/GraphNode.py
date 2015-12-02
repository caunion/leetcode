__author__ = 'Daoyuan'
from BaseSolution import *

class GraphNode:
    def __hash__(self):
        return self.x

    def __str__(self):
        return str(self.x)

    def __init__(self, val = None):
        self.x  = val
        self.neighbors = []
        self.p = None
        self.c = 0
        self.d = -1
        self.f = -1
        #for prim
        self.key = 2<<31


class Graph():
    V = {}
    weighted = False
    def __init__(self, V={}, with_weight = False):
        self.V = V
        self.weighted = with_weight
    @staticmethod
    def deserialize(g, make_symetery = False, with_weight = False):
        if len(g) == 1: return Graph({})
        if g[0] == "{" or g[0] == "[": g = g[1:-1]
        if len(g) == 0: return Graph({})
        nodes= {}
        for c in g.split('#'):
            segs = c.split(',')
            node = GraphNode( int(segs[0]) )
            node.neighbors = []
            nodes[ node.x ] = node

        for c in g.split('#'):
            segs = c.split(',')
            node = nodes[ int(segs[0]) ]
            for i in xrange(1, len(segs)):
                if with_weight:
                    other, weight = segs[i].split("@")
                    other = nodes[int(other)]
                    next = [other, float(weight)]
                    this = [node, float(weight)]
                else:
                    next = nodes[int(segs[i])]
                    other = next
                    this = node
                node.neighbors.append( next )
                if make_symetery and node.x != other.x:
                    other.neighbors.append( this )
        for node in nodes.values():
            node.neighbors = list(node.neighbors)
        graph = Graph(V=nodes, with_weight= with_weight)
        return graph

    def serialize(self, make_non_symetry = False, show_weight = True):
        result = []
        if make_non_symetry:
            graph = self.copy()
            for node in graph.V.values():
                for other in node.neighbors:
                    if self.weighted:
                        next, weight = other
                        this = [node, weight]
                    else:
                        next = other
                        this = node
                    if next.x != node.x: # keep self edge
                        graph.V[next.x].neighbors.remove(this)
        else:
            graph = self
        for node in graph.V.values():
            if self.weighted:
                node.neighbors = sorted(node.neighbors,key = lambda a: a[0].x)
            else:
                node.neighbors  = sorted(node.neighbors, key = lambda a: a.x)

            if self.weighted and show_weight:
                ret = ",".join([str(node.x), ]+[  str(other[0].x)+"@"+str(other[1]) for other in node.neighbors])
            else:
                ret = ",".join([str(node.x), ]+[  str(other.x) for other in node.neighbors])
            result.append(ret)
        result = "#".join( result)
        return "{"+ result +"}"

    def init(self):
        for node in self.V:
            node.c = 0
            node.p = None

    def copy(self):
        if len(self.V) == 0 : return Graph({},self.weighted)
        newnodes = {}
        for node in self.V.values():
            newnodes[node.x] = GraphNode(node.x)

        for node in self.V.values():
            if node.c == 0:
                queue = [ node ]
                while len(queue) > 0:
                    top = queue.pop(0)
                    top.c = 1
                    for other in top.neighbors:
                        if self.weighted:
                            n, weight = other
                            next = [newnodes[n.x], weight]
                        else:
                            n = other
                            next = newnodes[n.x]

                        if n.c == 0:
                            n.c = 1
                            queue.append( n )
                        newnodes[top.x].neighbors.append( next )
        newgraph = Graph(newnodes)
        return newgraph

class GraphTest(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (Graph.deserialize("{}", True), True),
            expects = "{}_{}"
        )
        self.push_test(
            params = (Graph.deserialize( "{0,1,2,3#3,1#4#1,2#2,2}"), False),
            expects =  "{0,1,2,3#1,2#2,2#3,1#4}_{0,1,2,3#1,2#2,2#3,1#4}"
        )
        self.push_test(
            params = (Graph.deserialize( "{0,1,2,3#3,1#4#1,2#2,2}", True), True),
            expects =  "{0,1,2,3#1,0,2,3#2,0,1,2#3,0,1#4}_{0,1,2,3#1,2,3#2,2#3#4}"
        )
        self.push_test(
            params = (Graph.deserialize( "{0,1@1.1,2@-2.1,3@3.1#3,1@-1.2#4#1,2@2.2#2,2@2.3}", True, True), True),
            expects =  "{0,1@1.1,2@-2.1,3@3.1#1,0@1.1,2@2.2,3@-1.2#2,0@-2.1,1@2.2,2@2.3#3,0@3.1,1@-1.2#4}_{0,1@1.1,2@-2.1,3@3.1#1,2@2.2,3@-1.2#2,2@2.3#3#4}"
        )
        self.push_test(
            params = (Graph.deserialize( "{0,1@1.1,2@-2.1,3@3.1#3,1@-1.2#4#1,2@2.2#2,2@2.3}", False, True), False),
            expects =  "{0,1@1.1,2@-2.1,3@3.1#1,2@2.2#2,2@2.3#3,1@-1.2#4}_{0,1@1.1,2@-2.1,3@3.1#1,2@2.2#2,2@2.3#3,1@-1.2#4}"
        )

    def solution(self, G, synmetry):
        return G.serialize() + "_" + G.serialize(make_non_symetry= synmetry)