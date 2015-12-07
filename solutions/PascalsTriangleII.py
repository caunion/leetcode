__author__ = 'Daoyuan'
from BaseSolution import *
class PascalsTriangleII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, rowIndex):
        if rowIndex < 0: return []
        result = [0] * (rowIndex+1)
        result[0] = 1
        for i in range(1, rowIndex+1):
            result[i] = result[i-1] * (rowIndex - i + 1) / i
        return result