__author__ = 'Daoyuan'
from BaseSolution import *
class Triangle(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([[2], [3,4],[6,5,7],[4,1,8,3]],),
            expects = 11
        )
    def solution(self,triangle):
        if not triangle: return 0
        n = len(triangle)
        m = len(triangle[n-1])
        c = [[0] * m for i in xrange(n)]
        c[0][0] = triangle[0][0]
        for i in xrange(1,n):
            k = len(triangle[i]) -1
            c[i][0] = triangle[i][0] + c[i-1][0]
            c[i][k] = triangle[i][k] + c[i-1][k-1]
        for i in xrange(1,n):
            k = len(triangle[i])
            for j in xrange(1,k-1):
                c[i][j] = min( c[i-1][j-1] + triangle[i][j], c[i-1][j]+ triangle[i][j])

        return min(c[n-1])

    def solution(self, triangle):
        if not triangle: return 0
        n = len(triangle)
        c =[ [1<<30] * (n+1) for i in xrange(2) ]
        c[0][0] = c[1][0]= triangle[0][0]
        for i in xrange(1,n):
            k = len(triangle[i])
            for j in xrange(k):
                if j == 0:
                    c[1][j] = c[0][j] + triangle[i][j]
                elif j==k-1:
                    c[1][j] = c[0][j-1] + triangle[i][j]
                else:
                    c[1][j] = min( c[0][j-1]+ triangle[i][j], c[0][j] + triangle[i][j] )
            for l in range(0, n+1):
                c[0][l] = c[1][l]

        return min(c[1])


