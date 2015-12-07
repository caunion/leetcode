__author__ = 'Daoyuan'
from BaseSolution import *
class PascalsTriangle(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (4,),
            expects = [[1],[1,1],[1,2,1],[1,3,3,1]]
        )
    def solution(self, numRows):
        if numRows <= 0: return []
        n = numRows
        result = [[1]]
        for i in range(1, n):
            ret = [1] * (i+1)
            for j in range(1,i):
                ret[j] = result[-1][j-1] + result[-1][j]
            result.append(ret)
        return result