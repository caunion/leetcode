__author__ = 'Daoyuan'
from BaseSolution import *
class UniquePaths(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, m, n):
        mul, div = 1, 1
        c, d = min(m-1,n-1), m+n-2
        for i in range(1, c+1):
            mul = mul * d
            d -= 1
            div = div* i
        return mul / div