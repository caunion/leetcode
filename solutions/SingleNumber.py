__author__ = 'Daoyuan'
from BaseSolution import *
class SingleNumber(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,2,3,2,1],),
            expects = 3
        )
    def solution(self, nums):
        ret = 0
        for i in nums:
            ret ^= i
        return ret