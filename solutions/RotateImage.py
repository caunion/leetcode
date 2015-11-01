__author__ = 'Daoyuan'
from BaseSolution import *

class RotateImage(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([[1,2],
                       [3,4]],),
            expects = [[3,1],
                       [4,2]]
        )

    def solution(self, matrix):
        back = [row[:] for row in matrix]
        self.inplace_rotate(matrix,back)
        return matrix
    def inplace_rotate(self,matrix, back):
        n = len(matrix)
        for i in range(0, n):
            for j in range(0, n):
                matrix[j][n-i -1] = back[i][j]
        return