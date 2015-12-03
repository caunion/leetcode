__author__ = 'Daoyuan'
from BaseSolution import *
class BurstBalloons(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        self.push_test(
            params = ([3,1,5,8],),
            expects = 167
        )
    def solution(self, nums):
        if not nums or nums == []: return 0
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        c = [[0] * (n+2) for i in xrange(n+2)]
        p = [[0] * (n+2) for i in xrange(n+2)]
        for i in range(1, n+1):
            c[i][i] = nums[i-1]*nums[i]*nums[i+1]
        for l in range(1, n):
            for i in range(1, n + 1 - l):
                j = i+l
                for k in range(i, j+1):
                    val = c[i][k-1] + c[k+1][j] + nums[i-1] * nums[k] * nums[j+1]
                    if val > c[i][j]:
                        c[i][j] = val
                        p[i][j] = k
        return c[1][n]