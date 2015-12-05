__author__ = 'Daoyuan'
from ..BaseSolution import *
class RangeMinimumQuery(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([0,3,1,4,5,5,-1,1,3,5,6,7,5],[(0,2),(1,4),(0,3),(3,9)]),
            expects = [0,1,0,-1]
        )

    def solution(self, nums, query):
        if not nums or len(nums) == 0: return -1
        d = self.init(nums)
        ret = []
        for q in query:
            k = 0
            left, right = q
            while 1<<(k+1) < right - left + 1:
                k += 1
            ret.append( min( d[left][k], d[ right - (1<<(k)) + 1][k]) )
        return ret
    def init(self, nums):
        n = len(nums)
        d = [[1<<30] * n for i in xrange(n)]
        for i in xrange(n):
            d[i][0] = nums[i]

        j = 1
        while 1<<j < n:
            i = 0
            while i + (1<<j) -1 < n:
                d[i][j] = min( d[i][j-1], d[i+ (1<<(j-1))][j-1] )
                i+=1
            j+=1
        return d