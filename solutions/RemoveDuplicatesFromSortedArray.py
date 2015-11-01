__author__ = 'Daoyuan'
from BaseSolution import *

class RemoveDuplicatesFromSortedArray(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ([1,1,2,2,2,2,3,3,3],),
            expects = 3
        )

    def solution(self, nums):
        last = -1e9
        j = -1
        for i in nums:
            if i == last:
                continue
            last = i
            j=j+1
            nums[j] = i
        return j+1
