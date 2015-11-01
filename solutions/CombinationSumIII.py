__author__ = 'Daoyuan'
from BaseSolution import *
class CombinationSumIII(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (3,15,),
            expects = [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]
        )
        self.push_test(
            params = (3,7,),
            expects = [[1,2,4]]
        )
        self.push_test(
            params = (3,9,),
            expects = [[1,2,6], [1,3,5], [2,3,4]]
        )
        self.push_test(
            params = (1,10,),
            expects = []
        )
        self.push_test(
            params = (6,43,)
        )

    def solution(self, k, n):
        ret = [item for item in self.combine( range(1,10), k, n) ]
        return ret

    def combine(self, nums, k, n):
        out = False
        for i in xrange(len(nums)):
            if k == 1 and n == nums[i]:
                out = True
                break
            else:
                for next in self.combine( nums[i+1:], k - 1, n - nums[i]):
                    yield [nums[i],] + next
        if out:
            out = False
            yield [nums[i],]
