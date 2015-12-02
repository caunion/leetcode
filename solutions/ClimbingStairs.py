__author__ = 'Daoyuan'
from BaseSolution import *
class ClimbingStairs(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (11,),
            expects = 144
        )

    def solution(self, n):
        if n <= 0: return 0
        s = [0] * (n+1)
        s[1] = 1
        if n == 1: return s[1]
        s[2] = 2
        for i in range(3, n+1):
            s[i] = s[i-1]+s[i-2]
        return s[n]

