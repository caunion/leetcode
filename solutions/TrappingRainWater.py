__author__ = 'Daoyuan'
from BaseSolution import *

class TrappingRainWater(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([0,1,0,2,1,0,1,3,2,1,2,1],),
            expects = 6
        )

    def solution(self, height):
        idx = 0
        length = len(height)