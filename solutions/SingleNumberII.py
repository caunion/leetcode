__author__ = 'Daoyuan'
from BaseSolution import *
class SingleNumberII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 8
        self.push_test(
            params = ([1,2,3,123,3,2,1,1,2,3],),
            expects = 123
        )
    def solution(self, nums):
        b0, b1 = 0, 0
        for num in nums:
            nb0 = (~b1 & b0 & ~num) | (~b1 & ~b0 & num)
            nb1 = (b1 & ~b0 & ~num) | (~b1 & b0 & num)
            b0, b1 = nb0, nb1
        return b0