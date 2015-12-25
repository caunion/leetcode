from BaseSolution import *
class SetMatrixZeroes(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ([[0,1,2,4],[1,0,0,1],[1,2,3,3],[1,2,3,1]],),
            expects=[[0,0,0,0],[0,0,0,0],[0,0,0,3],[0,0,0,1]]
        )

    def solution(self, matrix):
        if not matrix or len(matrix) == 0: return
        n = len(matrix)
        m = len(matrix[0])
        cols = set()
        rows = set()
        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    cols.add(j)
                    rows.add(i)
        for col in cols:
            for i in range(n):
                matrix[i][col] = 0
        for row in rows:
            for i in range(m):
                matrix[row][i] = 0
        return