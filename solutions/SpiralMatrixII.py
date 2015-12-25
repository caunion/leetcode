from BaseSolution import *
class SpiralMatrixII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (5,),
            expects = [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
        )
    def solution(self, n):
        import math
        if n <= 0: return []
        matrix = [ [0] * n for i in range(n)]
        m = n
        num = 1
        for offset in range(0, int(math.ceil(min(m, n) / 2.0))):
            for j in range(0+offset, m - offset):
                i = 0 + offset
                matrix[i][j] = num
                num += 1
            for i in range(0+offset + 1, n - offset):
                j = m - offset - 1
                matrix[i][j] = num
                num += 1
            for j in range(m-offset-2, 0+offset-1, -1):
                i = n - offset - 1
                if i == 0 + offset: break
                matrix[i][j] = num
                num += 1
            for i in range(n - offset - 2, 0+offset, -1):
                j = 0 + offset
                if j == m - offset -1: break
                matrix[i][j] = num
                num += 1
        return matrix
