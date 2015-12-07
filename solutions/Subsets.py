__author__ = 'Daoyuan'
from BaseSolution import *
class Subsets(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([0,1,2,3],),
            expects = [[],[3],[2],[2,3],[1],[1,3],[1,2],[1,2,3],[0],[0,3],[0,2],[0,2,3],[0,1],[0,1,3],[0,1,2],[0,1,2,3]],
            expect_unordered= True
        )
    def solution(self, nums):
        if not nums or len(nums) == 0: return [[]]
        result = [[]]
        n = len(nums)
        nums = sorted(nums)
        for i in range(1, n+1):
            for next in self.combination(nums, 0, n-1, i):
                result.append(next)
        return result
    def combination(self, nums, left, right, n):
        if n<=0 or right - left + 1< n:
            yield []
        elif right - left + 1== n:
            yield nums[left : right+1]
        else:
            for next in self.combination(nums, left+1, right, n):
                yield next
            for next in self.combination(nums, left+1, right, n-1):
                yield [nums[left], ] + next