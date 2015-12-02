__author__ = 'Daoyuan'
from ..BaseSolution import *
from ..GraphNode import *

class C22_2_9_TraverseTwice(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (Graph.deserialize( "{0,1#1,2,3#2,4#3,4#4,5#5}", True), ),
            expects =  "0-1 1-2 2-4 4-3 3-4 4-5 5-4 4-2 2-1 1-3 3-1 1-0"
        )
        self.push_test(
            params = (Graph.deserialize( "{0,1#1,2,5#2,4#5,4#4,3#3}", True), ),
            expects =  "0-1 1-2 2-4 4-3 3-4 4-5 5-4 4-2 2-1 1-5 5-1 1-0"
        )
    def solution(self, G):
        self.path = []
        for node in G.V.values():
            if node.c == 0:
                node.c = 1
                self.dfs_visit(node)
                node.c = 2
        return " ".join(self.path)

    def dfs_visit(self, node):
        for next in node.neighbors:
            if next.c == 0:
                next.c = 1
                self.path.append( str(node.x) + "-" + str(next.x))
                self.dfs_visit(next)
                next.c = 2
                self.path.append( str(next.x) + "-" + str(node.x) )
            elif next.c == 2: # trick
                self.path.append( str(node.x) + "-" + str(next.x))
                self.path.append( str(next.x) + "-" + str(node.x))

