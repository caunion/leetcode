__author__ = 'Daoyuan'

from BaseSolution import *

class Sqrt(BaseSolution):
    """

    newtown method, iterative

    medium
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test((125348,), 354)
        self.push_test((0,), 0)
        self.push_test((2,), 1)
        self.push_test((3,), 2)
        self.push_test((1,), 1)

    def solution(self, x):
        x0 = x1 = x/2
        if x <= 0 :
            return 0
        if x0 == 0:
            return 1
        while True:
            x1 = self.newtown(x0, x)
            if abs(x1 - x0)< 1:
                break
            else:
                x0 = x1
        return int(x1)
    def newtown(self, x, s):
        return 0.5 * (x + s / (x * 1.0))

