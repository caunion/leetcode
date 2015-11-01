__author__ = 'Daoyuan'
from BaseSolution import *

class CombinationSumII(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([10,1,2,7,6,1,5], 8,),
            expects = [
                [1, 7],
                [1, 2, 5],
                [2, 6],
                [1, 1, 6],
            ],
            expect_unordered = True
        )
        self.push_test(
            params = ([4,3,2,1,1], 5,),
            expects = [
                [1, 4],
                [1, 1, 3],
                [2, 3],
            ],
            expect_unordered = True
        )
        self.push_test(
            params = ([2],5),
            expects = []
        )

    def solution(self, candidates, target):
        nums = sorted(candidates)
        return list(self.combine(nums, target))

    def combine(self, nums, target):
        if len(nums) == 0:
            return
        last = -1
        for i in xrange(len(nums)):
            if last == nums[i]:
                continue
            last = nums[i]
            if nums[i] == target:
                yield [nums[i],]
            elif nums[i] > target:
                return
            else:
                for next in self.combine( nums[i+1:], target - nums[i]):
                    yield [nums[i],] + next