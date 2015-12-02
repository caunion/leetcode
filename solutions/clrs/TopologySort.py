__author__ = 'Daoyuan'
from solutions.BaseSolution import  *
from ..GraphNode import *

class TopologySort(BaseSolution):
    def __int__(self):
        BaseSolution.__init__(self)


    def solution(self, edges):
        V = {}
        for edge in edges:
            if edge[0] not in V:
                V[edge[0]] = GraphNode(edge[0])
            if edge[1] not in V:
                V[edge[1]] = GraphNode(edge[1])
            V[edge[0]].nextList.append(V[edge[1]])

