__author__ = 'Daoyuan'
from BaseSolution import *
class ContainsDuplicateII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params=([1,2,3,4,5,6,1,2,3,4],6),
            expects = True
        )
        self.push_test(
            params=([1,2,3,4,5,6,7,1,2,3,4],6),
            expects = False
        )

    def solution(self, nums, k):
        dic = {}
        if not nums: return False
        for i,num in enumerate(nums):
            if not num in dic:
                dic[num] = i
            elif i - dic[num] <= k:
                return True
            else:
                dic[num] = i
        return False