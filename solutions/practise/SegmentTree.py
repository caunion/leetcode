__author__ = 'Daoyuan'
from ..BaseSolution import *
class SegmentTree(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([9,6,7,8,5,4,3,2],[(0,3),(1,5),(1,7),(-1<<30, 2, 0),(-1<<30, 7, 5),(0,3),(1,5),(3,7)]),
            expects = [6,4,2,0,0,3]
        )

    def solution(self, nums, query):
        self.tree, self.left, self.right= self.buildTree(nums)
        result = []
        for q in query:
            if len(q) == 2:
                l, r = q
                ret = self.query(l,r,1)
                result.append(ret)
            else:
                _, p, v = q
                self.update(p, v, 1)
        return result


    def buildTree(self, nums):
        n = len(nums)
        tree = [0] * (2*n)
        left = [0]* (2*n)
        right= [0]* (2*n)
        for i in xrange(n, 2*n):
            tree[i] = nums[i-n]
            left[i] = right[i] = i - n

        height = 0
        while 1<<(height+1) <= n: height += 1
        for h in range(height -1, -1, -1):
            l = 1<<h
            r = 1<<(h+1)
            for i in xrange(l, r):
                if i * 2 < 2*n and i * 2 + 1 < 2*n:
                    tree[i] = min(tree[i*2], tree[i*2+1])
                    left[i] = (i - l) * (1<<(height- h))
                    right[i] = (i- l) * (1<<(height- h)) + (1<< (height -h)) -1
        return tree, left, right

    def query(self, L, R, node):
        l = self.left[node]
        r = self.right[node]
        m = ( r - l ) / 2 + l
        ret = 1<<30
        if L <= l and r <= R: return self.tree[node]
        if L <= m:  ret = min(self.query(L, R, node * 2), ret)
        if m+1 <= R: ret = min(self.query(L, R,node*2 + 1), ret)
        return ret

    def update(self, idx, v, node):
        if self.left[node] == self.right[node]:
            self.tree[node] = v
        else:
            m = ( self.right[node] -self.left[node]) / 2 + self.left[node]
            if idx > m:
                self.update(idx, v, node*2+1)
            else:
                self.update(idx, v, node*2)
            self.tree[node] = min(self.tree[node*2], self.tree[node*2+1])

