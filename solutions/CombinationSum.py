__author__ = 'Daoyuan'
from BaseSolution import *
class CombinationSum(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 8
        self.push_test(
            params = ([2,3,6,7],7),
            expects = [
                [7],
                [2,2,3]
            ]
        )
        self.push_test(
            params = ([3,2,6,7],7),
            expects = [
                [7],
                [2,2,3]
            ]
        )
        self.push_test(
            params = ([2],7),
            expects = []
        )
        self.push_test(
            params = ([],7),
            expects = []
        )
    def solution(self, candidates, target):
        nums = sorted(candidates)
        return list( self.combinesum(nums, target))

    def combinesum(self, nums, target):
        for i in xrange( len(nums) -1, -1, -1):
            if target  == nums[i]:
                yield [nums[i],]
            elif target < nums[i]:
                continue
            elif target > nums[i]:
                for item in self.combinesum(nums[0:i+1], target - nums[i]):
                    yield  item +[ nums[i],]