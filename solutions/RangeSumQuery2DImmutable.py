__author__ = 'Daoyuan'
from BaseSolution import *

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix or matrix == []:
            self.n = 0
            self.m = 0
            return

        n = len(matrix)
        m = len(matrix[0])
        s = [[0] * (m+1) for i in xrange(n+1)]
        for i in xrange(n):
            for j in xrange(m):
                if i == 0 and j==0:
                    s[1][1] = matrix[0][0]
                elif i == 0:
                    s[1][j+1] = s[1][j] + matrix[0][j]
                elif j == 0:
                    s[i+1][1] = s[i][1] + matrix[i][0]
                else:
                    s[i+1][j+1] = s[i+1][j] + s[i][j+1] + matrix[i][j] - s[i][j]
        self.s = s
        self.m = m
        self.n = n
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if  0 <= row2 < self.n and \
            0 <= row1 < self.n and \
            0 <= col1 < self.m and \
            0 <= col2 < self.m:

            if row2<row1 or col2 < col2: return 0
            row2+=1
            col2+=1
            return self.s[row2][col2] + self.s[row1][col1] - self.s[row1][col2] - self.s[row2][col1]
        else:
            return  -1
class RangeSumQuery2DImmutable(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ( [
                          [3, 0, 1, 4, 2],
                          [5, 6, 3, 2, 1],
                          [1, 2, 0, 1, 5],
                          [4, 1, 0, 1, 7],
                          [1, 0, 3, 0, 5]
                        ],[(2,1,4,3),(1,1,2,2),(1,2,2,4)]),
            expects = [8,11,12]
        )
    def solution(self, matrix, query):
        ret = []
        mat = NumMatrix(matrix)
        for q in query:
            ret.append(mat.sumRegion(*q))
        return ret