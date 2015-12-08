from BaseSolution import *
class SummaryRanges(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([0,1,2,4,5,7],),
            expects= ["0->2","4->5","7"]
        )

    def solution(self, nums):
        if not nums or len(nums) == 0: return []
        n = len(nums)
        result = []
        start = end = nums[0]
        for i in xrange(1, n):
            num = nums[i]
            if num - end == 1:
                end = num
            else:
                if end> start:
                    result.append("%d->%d" %(start, end))
                else:
                    result.append("%d" %(start))
                start = end = num
        if end> start:
            result.append("%d->%d" %(start, end))
        else:
            result.append("%d" %(start))
        return result