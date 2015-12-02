__author__ = 'Daoyuan'
from BaseSolution import *
class MinimumPathSum(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([[0,1],[1,0]],),
            expects = 1
        )
    def solution(self, grid):
        if not grid or grid == []:
            return 0
        m = len(grid)
        n = len(grid[0])
        s = [[1<<30] * n for i in xrange(m)]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    s[0][0] = grid[0][0]
                elif i == 0:
                    s[0][j] = s[0][j-1] + grid[0][j]
                elif j == 0:
                    s[i][0] = s[i-1][0] + grid[i][0]
                else:
                    s[i][j] = min(s[i-1][j]+ grid[i][j], s[i][j-1]+grid[i][j])

        return s[m-1][n-1]