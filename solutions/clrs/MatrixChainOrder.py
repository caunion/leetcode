__author__ = 'Daoyuan'
from ..BaseSolution import *

class MatrixChainOrder(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([30, 35, 15, 5,10,20,25],),
            expects = (15125, "((M1(M2M3))((M4M5)M6))")
        )
        self.push_test(
            params = ([5,10,3,12,5,50,6],),
            expects = (2010, '((M1M2)((M3M4)(M5M6)))')
        )
    def solution(self, M):
        return self.matrixChainRec(M)
        #return self.matrixChainIter(M)

    def matrixChainRec(self, M):
        n = len(M)
        m = [ [1<<30] * n for i in xrange(n)]
        s = [ [-1] * n for i in xrange(n)]

        for i in xrange(n):
            m[i][i] = 0
        self.M = M
        self.s = s
        self.m = m
        self.matrixChainRecursive(1,n-1)
        minval = self.m[1][n-1]
        result = self.getParents(self.s, 1, n-1)
        return (minval, result)

    def matrixChainRecursive(self, left, right):
        if left == right:
            self.m[left][right] = 0
        else:
            for k in xrange(left, right):
                if self.m[left][k] == 1<<30:
                    self.matrixChainRecursive(left, k)
                if self.m[k+1][right] == 1<<30:
                    self.matrixChainRecursive(k+1,right)
                q = self.m[left][k] + self.m[k+1][right] + self.M[left-1] * self.M[k] * self.M[right]
                if q < self.m[left][right]:
                    self.m[left][right] = q
                    self.s[left][right] = k


    def matrixChainIter(self, M):
        n = len(M)
        m = [ [ 1<< 30 ] * n for i in xrange(n) ]
        s = [ [-1] * n for i in xrange(n) ]

        for i in xrange(n):
            m[i][i] = 0

        for l in range(2, n):
            for i in range(1, n- l + 1):
                j = i + l -1
                m[i][j] = 1 << 30
                for k in range(i,j):
                    tmp = m[i][k] + m[k+1][j] + M[i-1] * M[k] * M[j]
                    if m[i][j] > tmp:
                        m[i][j] = tmp
                        s[i][j] = k

        minval = m[1][n-1]
        result = self.getParents(s, 1, n-1)
        return (minval, result)

    def getParents(self, s, left, right):
        if left ==  right:
            return "M%d" % left
        else:
            return  "(" + \
                  self.getParents(s, left, s[left][right]) + \
                  self.getParents(s, s[ left ][ right] + 1, right) +\
                  ")"
