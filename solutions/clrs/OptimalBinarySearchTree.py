__author__ = 'Daoyuan'
from ..BaseSolution import *
from ..TreeNode import *
class OptimalBinarySearchTree(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([0.15, 0.10, 0.05, 0.10, 0.20],[0.05, 0.10, 0.05, 0.05, 0.05, 0.10],),
            expects = (2.75,"{k2,k1,k5,#,#,k4,#,k3}")
        )

    def solution(self, p, q):
        return self.obstRec(p,q)
        return self.obstIter(p,q)

    def obstRec(self, p, q):
        p = [0, ] + p
        n = len(p)
        e = [ [1<<30] * n for i in xrange(n+1) ]
        w = [ [0]* n for i in xrange(n+1)]
        root = [ [-1] * n for i in xrange(n+1)]
        for i in range(1, n+1):
            e[i][i-1] = q[i-1]
            w[i][i-1] = q[i-1]

        for l in range(0, n-1):
            for i in range(1, n-l):
                j = i+l
                w[i][j] = w[i][j-1] + p[j] + q[j]
        self.p = p
        self.q= q
        cost = self.obstRecurssive(e,w,root, 1, n-1)
        tree = self.rebuildTree(root, 1, n-1)
        return (cost, tree)

    def obstRecurssive(self, e, w, root, left, right):
        if e[left][right] < (1<<30) -1:
            return e[left][right]
        if left == right + 1:
            return e[left][right]
        else:
            for r in range(left, right+1):
                t = self.obstRecurssive(e,w,root,left,r-1) + self.obstRecurssive(e,w,root,r+1,right) + w[left][right]
                if e[left][right] > t:
                    e[left][right] = t
                    root[left][right] = r
            return e[left][right]

    def obstIter(self, p, q):
        p = [0,] + p
        n = len(p)
        e = [[1<<30] * n for i in xrange(n+1)]
        w = [[0]*n for i in xrange(n+1)]
        root = [[-1] *n for i in xrange(n+1)]
        for i in range(1,n+1):
            e[i][i-1] = q[i-1]
            w[i][i-1] = q[i-1]
        for l in range(0, n-1):
            for i in range(1, n-l):
                j = i+l
                w[i][j] = w[i][j-1] + p[j] + q[j]
                for r in range(i, j+1):
                    tmp = e[i][r-1] + e[r+1][j] + w[i][j]
                    if tmp < e[i][j]:
                        e[i][j] = tmp
                        root[i][j] = r
        allcost = e[1][n-1]
        tree = self.rebuildTree(root, 1, n-1)
        return (allcost, tree)
    def rebuildTree(self, root, left, right):
        queue = [(left, right)]
        ret = []
        while len(queue) > 0:
            top = queue.pop(0)
            left, right = top[0], top[1]
            val = root[left][right]
            if val > 0:
                ret.append("k%d"%val)
            else:
                ret.append("#")
                continue
            queue.append( (left, val-1) )
            queue.append( (val+1, right) )
        result = ",".join(ret)
        return "{" + result.strip(",#") + "}"

    def inOrderPrint(self, root, left, right):
        if left > right:
            return ""
        elif left == right:
            return "k%d" % left
        else:
            ret = [self.rebuildTree(root, left, root[left][right]-1),
                   "k%d" % root[left][right],
                   self.rebuildTree(root, root[left][right]+1, right)]
            return ",".join(ret)
