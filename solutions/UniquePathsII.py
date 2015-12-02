__author__ = 'Daoyuan'
from BaseSolution import *
class UniquePathsII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([[0,1]],),
            expects = 0
        )
    def solution(self, obstacleGrid):
        if not obstacleGrid: return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        for i in xrange(n):
            for j in xrange(m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1

        if obstacleGrid[0][0] == -1:
            obstacleGrid[0][0] = 0
        else:
            obstacleGrid[0][0] = 1

        for i in xrange(1,n):
            if obstacleGrid[i][0] == -1:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
        for j in xrange(1,m):
            if obstacleGrid[0][j] == -1:
                obstacleGrid[0][j] = 0
            else:
                obstacleGrid[0][j] = obstacleGrid[0][j-1]
        for i in xrange(1,n):
            for j in xrange(1,m):
                if obstacleGrid[i][j] == -1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] =  obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

        return obstacleGrid[n-1][m-1]


