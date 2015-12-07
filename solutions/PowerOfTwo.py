__author__ = 'Daoyuan'
from BaseSolution import *
class PowerOfTwo(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, n):
        flag = False
        if n < 0: return flag
        for i in range(0,31):
            if (1<<i) & n:
                if not flag:
                    flag = True
                else:
                    return False
        return flag