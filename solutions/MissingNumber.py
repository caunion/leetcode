from BaseSolution import *
class MissingNumber(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,2,3,4,0,6,7],),
            expects= 5
        )
    def solution(self, nums):
        n = len(nums)
        return n * (1+n) / 2 - sum(nums)

    def solution(self, nums):
        ret = len(nums)
        for i in range(len(nums)):
            ret ^= nums[i]
            ret ^= i
        return ret