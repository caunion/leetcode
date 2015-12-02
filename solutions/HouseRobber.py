__author__ = 'Daoyuan'
from BaseSolution import *
class HouseRobber(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,2,3,1,2,3,5,3,2,5,6,3,3,5,6,7,4,2,1,4,6,7,4,2,4,7,3],),
            expects = 53
        )
    def solution(self, nums):
        if not nums or nums == []: return 0
        n = len(nums)
        s = [0] * n
        s[0] = nums[0]
        if n > 1:
            s[1] = max(nums[0], nums[1])
            for i in range(2, n):
                s[i] = max(s[i-1], nums[i] + s[i-2])
        return s[n-1]