__author__ = 'Daoyuan'
from BaseSolution import *
class SingleNumberIII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([-1,0,-1,0,1,2,3,122,333,3,2,1],),
            expects = [122,333],
            expect_unordered= True
        )
    def solution(self, nums):
        diff = 0
        for num in nums:
            diff ^= num
        diff = diff&-diff
        a, b = 0, 0
        for num in nums:
            if diff & num == 0:
                a ^= num
            else:
                b ^= num
        return [a,b]