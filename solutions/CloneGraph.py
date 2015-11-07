__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *

class UndirectedGraphNode(object):
    def __init__(self, x=-1e9):
        self.label = x
        self.neighbors = []

class CloneGraph(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, node):
        if node:
            node = self.bfs(node)
        return node

    def bfs(self, node):
        new = UndirectedGraphNode(node.label)
        visited = {new.label:new}
        queue = [node]
        while len(queue) > 0:
            top = queue.pop(0)
            for n in top.neighbors:
                if n.label not in visited:
                    newn = UndirectedGraphNode(n.label)
                    visited[newn.label] = newn
                    queue.append(n)
                else:
                    newn = visited[n.label]
                visited[top.label].neighbors.append(newn)
        return new