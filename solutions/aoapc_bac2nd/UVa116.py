from ..BaseSolution import *
class UVa116(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([[3,4,1,2,8,6],
                       [6,1,8,2,7,4],
                       [5,9,3,9,9,5],
                       [8,4,1,3,2,6],
                       [3,7,2,8,6,4]],),
            expects = (16, [(0, 0), (1, 1), (2, 2), (3, 3), (3, 4), (4, 5)])
        )
        self.push_test(
            params = ([[3,4,1,2,8,6],
                      [6,1,8,2,7,4],
                      [5,9,3,9,9,5],
                      [3,4,1,3,2,6],
                      [3,7,2,1,2,3]],),
            expects = (11, [(0, 0), (1, 1), (0, 2), (4, 3), (3, 4), (4, 5)])
        )
    def solution(self, matrix):
        inf = 1<<30
        if not matrix or len(matrix) == 0: return  -1
        n = len(matrix)
        m = len(matrix[0])
        next = [[inf] * m for i in xrange(n)]
        c = [[inf] * m for i in xrange(n)]

        c[n-1][m-1] = matrix[n-1][m-1]
        for j in range(m-2, -1, -1):
            for i in range(n-1, -1, -1):
                rows = [ (i-1+n) % n, i, (i+1)%n]
                for row in rows:
                    v = c[row][j+1]+ matrix[i][j]
                    if v < c[i][j]:
                        c[i][j] = v
                        next[i][j] = row
                    elif v == c[i][j]:
                        next[i][j] = min(next[i][j], row)
        path = [(0,0)]
        nextval = next[0][0]
        while nextval < inf:
            path.append( (nextval, len(path)))
            nextval = next[nextval][len(path)-1]
        return (c[0][0], path)