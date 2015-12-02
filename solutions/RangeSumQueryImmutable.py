__author__ = 'Daoyuan'
from BaseSolution import *

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        s = [0] * (n+1)
        for i in range(1,n+1):
            s[i] = s[i-1] + nums[i-1]
        self.s = s
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if j<i: return 0
        j+=1
        return self.s[j] - self.s[i]

class RangeSumQueryImmutable(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([-2, 0, 3, -5, 2, -1], [[2,2],[0,2],[2,5],[0,5]]),
            expects = [3,1,-1,-3]
        )
    def solution(self, nums, query):
        arr = NumArray(nums)
        ret = []
        for q in query:
            ret.append(arr.sumRange(*q))
        return ret