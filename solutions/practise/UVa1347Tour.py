from ..BaseSolution import *
import math
class UVa1347Tour(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([(1,7),(2,1),(3,4),(6,5),(7,1),(8,6),(9,3)],),
        )

    def solution(self, points):
        if not points or len(points) <= 1:
            return 0
        n = len(points)
        d = [ [ 1<<30 ] * n for i in xrange(n)]
        for i in range(1, n):
            d[n-1][i] = self.dist(points[n-1],points[i])
            d[i][n-1] = self.dist(points[n-1], points[i])

        for i in range(n-2, -1,-1):
            for j in xrange(0, i):
                d[i][j] = min(d[i+1][j] + self.dist(points[i], points[i+1]), d[i][i+1] + self.dist(points[j], points[i+1]))
        return d[0][0]

    def dist(self, points, i, j):
        return  math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)