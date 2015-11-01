__author__ = 'Daoyuan'
from BaseSolution import *

class MaximumSubarray(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([-2,1,-3,4,-1,2,1,-5,4],),
            expects = 6
        )
    def solution(self, nums):
        if len(nums) == 0 : return 0
        i = 0
        total = 0
        m = max(nums)
        while i < len(nums):
            temp = total + nums[i]
            if temp <=0:
                total = 0
            else:
                total = temp
                if temp > m:
                    m = temp
            i = i + 1
        return m