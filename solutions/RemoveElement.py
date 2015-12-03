__author__ = 'Daoyuan'
from BaseSolution import *
class RemoveElement(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
    def solution(self, nums, val):
        if not nums: return 0
        tmp = []
        for v in nums:
            if v != val:
                tmp.append(v)
        nums[:] = tmp[:]
        return len(tmp)