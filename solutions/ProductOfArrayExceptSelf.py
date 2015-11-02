__author__ = 'Daoyuan'
from BaseSolution import *

class ProductOfArrayExceptSelf(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,2,3,4],),
            expects = [24,12,8,6]
        )

    ## no division, O(1) space
    def solution(self, nums):
        zeros = 0
        length = len(nums)
        product = 1
        ret = [1] * length
        for i in xrange(1,len(nums)):
            if i==0:
                zeros = zeros+1
                continue
            ret[i] = ret[i-1] * nums[i-1]
        for i in xrange(len(nums) -1, 0, -1):
            if zeros > 1:
                nums[i] = 0
            else:
                nums[i-1] = nums[i] * nums[i-1]

        for i in xrange(length-1):
            ret[i] = ret[i] * nums[i+1]
        return ret