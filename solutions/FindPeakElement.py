__author__ = 'Daoyuan'
from BaseSolution import *
class FindPeakElement(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, nums):
        if not nums or len(nums) == 0: return -1
        if len(nums) == 1: return 0
        n = len(nums)
        for i in xrange(1, n):
            j = n - i
            if nums[j] > nums[j-1]: return j
            if nums[i-1] > nums[i]: return i-1
