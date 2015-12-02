__author__ = 'Daoyuan'
from ..BaseSolution import *

class LCS(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params=("ABCBDAB","BDCABA",),
            expects = [(4,"BCBA"),(4,"BDAB")],
            expect_oneof= True
        )

    def solution(self, x, y):
        return self.lcsRec(x,y)
        return self.lcsIter(x,y)

    def lcsRec(self, x, y):
        n = len(x)
        m = len(y)
        self.x = " " + x
        self.y = " " + y
        self.c = [[-1] * (m+1) for i in xrange(n+1)]
        self.b = [[-1] * (m+1) for i in xrange(n+1)]
        self.seq = ""
        length = self.lcsRecursive(n,m)
        seq = self.getSeq(self.b,n,m)
        return (length, seq)
    def lcsRecursive(self, n, m):
        if self.c[n][m] > 0:
            return self.c[n][m]
        if m == 0 or n == 0:
            self.c[n][m] = 0
        elif self.x[n] == self.y[m]:
            self.c[n][m] = self.lcsRecursive(n-1,m-1) + 1
            self.b[n][m] = 3
            self.lcsRecursive(n-1,m-1)
        elif self.lcsRecursive(n,m-1) < self.lcsRecursive(n-1,m):
            self.c[n][m] = self.c[n-1][m]
            self.b[n][m] = 1
        else:
            self.c[n][m] = self.c[n][m-1]
            self.b[n][m] = 2
        return self.c[n][m]

    def lcsIter(self, x, y):
        n = len(x)
        m = len(y)
        x = " " + x
        y = " " + y
        c = [[-1] * (m + 1) for i in xrange(n + 1)]
        b = [[-1] * (m + 1) for i in xrange(n + 1)]
        for i in xrange(n+1):
            c[i][0] = 0
        for i in xrange(m+1):
            c[0][i] = 0
        for i in xrange(1,n+1):
            for j in xrange(1,m+1):
                if x[i] == y[j]:
                    c[i][j] = c[i-1][j-1] + 1
                    b[i][j] = 3
                else:
                    l1 = c[i-1][j]
                    l2 = c[i][j-1]
                    if l1 > l2:
                        c[i][j] = l1
                        b[i][j] = 1
                    else:
                        c[i][j] = l2
                        b[i][j] = 2
        self.x = x
        self.y = y
        seq = self.getSeq(b, n, m)
        return (c[n][m], seq)

    def getSeq(self, b, n, m):
        if b[n][m] == 3:
            return self.getSeq(b, n-1, m-1) + self.x[n]
        elif b[n][m] == 2: return self.getSeq(b, n, m-1)
        elif b[n][m] == 1: return self.getSeq(b, n-1, m)
        else: return ""