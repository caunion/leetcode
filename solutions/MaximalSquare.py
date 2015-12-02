__author__ = 'Daoyuan'
from BaseSolution import *
class MaximalSquare(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (["0110111111111111110","1011111111111111111","1101111111110111111","1111111111111011111","1111111111111101111","1110111011111111101","1011111111111101111","1111111111111110110","0011111111111110111","1101111111011111111","1111111110111111111","0110111011111111111","1111011111111101111","1111111111111111111","1111111111111111111","1111111111111111101","1111111101101101111","1111110111111110111"],),
            expects = 25
        )
        self.push_test(
            params = (["0110010101","0010101010","1000010110","0111111010","0011111110","1101011110","0001100010","1101100111","0101101011"],),
            expects = 4
        )
        self.push_test(
            params = (["10111","01010","11011","11011","01111"],),
            expects = 4
        )
        self.push_test(
            params = (["0001","1101","1111","0111","0111"],),
            expects = 9
        )
        self.push_test(
            params=(['10100','10111','11111','10010'],),
            expects = 4
        )
    def solution(self, matrix):
        if not matrix or matrix == [] : return 0
        n = len(matrix)
        m = len(matrix[0])
        h = [[0] * m for i in xrange(n)]
        w = [[0] * m for i in xrange(n)]
        for i in xrange(n):
            if int(matrix[i][0]) == 1:
                h[i][0] = 1
                w[i][0] = 1
        for j in xrange(m):
            if int(matrix[0][j]) == 1:
                h[0][j] = 1
                w[0][j] = 1
        for i in xrange(1,n):
            for j in xrange(1, m):
                if int(matrix[i][j]) == 1:
                    h[i][j] = 1
                    w[i][j] = 1
                    if h[i-1][j] + 1 >= h[i][j-1]:
                        h[i][j] = max(h[i][j], h[i][j-1])
                    if w[i][j-1]+1>= w[i-1][j]:
                        w[i][j] = max(w[i][j], w[i-1][j])
                    if int(matrix[i-1][j-1]) == 1:
                        h[i][j] = max(h[i][j], min(h[i-1][j-1] + 1, h[i-1][j] + 1) )
                        w[i][j] = max(w[i][j], min(w[i-1][j-1] + 1, w[i][j-1] + 1) )

        ret = max([ min(w[i][j], h[i][j]) for j in xrange(m) for i in xrange(n)]) ** 2
        return ret