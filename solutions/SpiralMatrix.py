from BaseSolution import *
class SpiralMatrix(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],),
            expects= [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
        )
        self.push_test(
            params = ([[2,3]],),
            expects = [2,3]
        )
        self.push_test(
            params =  ([ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]],),
            expects = [1,2,3,6,9,8,7,4,5]
        )
    def solution(self, matrix):
        if not matrix or len(matrix) == 0: return []
        import math
        n, m = len(matrix), len(matrix[0])
        ret = []
        for offset in range(0, int(math.ceil(min(m, n) / 2.0))):
            for j in range(0+offset, m - offset):
                i = 0 + offset
                ret.append(matrix[i][j])
            for i in range(0+offset + 1, n - offset):
                j = m - offset - 1
                ret.append(matrix[i][j])
            for j in range(m-offset-2, 0+offset-1, -1):
                i = n - offset - 1
                if i == 0 + offset: break
                ret.append(matrix[i][j])
            for i in range(n - offset - 2, 0+offset, -1):
                j = 0 + offset
                if j == m - offset -1: break
                ret.append(matrix[i][j])
        return ret