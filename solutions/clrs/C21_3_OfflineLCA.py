__author__ = 'Daoyuan'
from DisjointSet import *
from ..BaseSolution import *
from ..TreeNode import *

class C21_3_OfflineLCA(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{1,2,3,4,5,6,7}"), [[5,4],[4,6], [5,3],[4,2]],),
            expects = [2,1,1,2]
        )
        self.push_test(
            params = (TreeNode.deserialize("{1,2,3,4,5,6,7,#,#,8,9,#,#,10,#,#,11,12,#,13,14}"), [[1,4],[2,3],[5,6],[11,12],[12,7],[6,14]],),
            expects = [1,1,1,5,1,3]
        )

    def solution(self, root, queries):
        self.queries = {}
        self.tree = self.bfs(root)
        for idx, query in enumerate(queries):
            if query[0] not in self.queries:
                self.queries[ query[0] ] = []
            if query[1] not in self.queries:
                self.queries[ query[1] ] = []
            self.queries[query[0]].append( (idx,query[1]) )
            self.queries[query[1]].append( (idx,query[0]) )
        self.result = { }
        self.dset = DisjointSet()
        self.lca(root)
        return self.result.values()
    def bfs(self,root):
        tree = {}
        queue = [root]
        while len(queue) > 0:
            top = queue.pop(0)
            if not top: continue
            tree[top.val] = top
            if top.left: queue.append(top.left)
            if top.right: queue.append(top.right)

        return tree
    def lca(self,root):
        u = self.dset.makeset( root.val )
        self.dset.findset(root.val).ancestor = u
        for node in (root.left, root.right):
            if not node: continue
            self.lca(node)
            self.dset.union( root.val, node.val)
            self.dset.findset(root.val).ancestor = u
        root.state = 2
        if root.val in self.queries:
            for idx,other in self.queries[ root.val ]:
                if self.tree[other].state == 2:
                    self.result[idx] = self.dset.findset( other ).ancestor.val
