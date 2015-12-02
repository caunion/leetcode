__author__ = 'Daoyuan'
from BaseSolution import *
import math
class MaximumProductSubarray(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        self.push_test(
            params =([2,3,-2,4],),
            expects = 6
        )
        self.push_test(
            params = ([-2,1,2,3,0,-1,-2,3,4,3,-1,2,3,0,-3],),
            expects = 432
        )
        self.push_test(
            params = ([-2,1,2,3,0,-2,-2,3,4,3,-4,2,3,0,-3],),
            expects = 1728
        )
        self.push_test(
            params = ([-2,1,2,3,0,-2,2,3,4,3,-4,2,3,0,-3],),
            expects = 3456
        )


    # beautiful DP algorithm

    def solution(self, nums):
        big = small = nums[0]
        maxv = minv = nums[0]
        for i in nums[1:]:
            big,small  = max(big * i, small*i, i),min(big * i, small * i ,i)
            maxv, minv = max(big, maxv), min(small, minv)
        return maxv

    def solution(self, nums):
        n = len(nums)
        high = [0] * n
        low = [0] * n
        high[0] = low[0] = nums[0]
        for i in range(1, n):
            if nums[i-1] == 0:
                high[i] = nums[i]
                low[i] = nums[i]
            else:
                high[i] = max( high[i-1]*nums[i], nums[i], low[i-1]*nums[i])
                low[i] = min(high[i-1]*nums[i], nums[i], low[i-1]*nums[i])
        return max(high)


















