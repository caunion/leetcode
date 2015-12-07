__author__ = 'Daoyuan'
from BaseSolution import *
class NumberOf1Bits(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, n):
        ret = 0
        for i in range(0,32):
            if (1<<i) & n:
                ret+=1
        return ret