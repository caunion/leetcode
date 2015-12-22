from BaseSolution import *
class MinimumSizeSubarraySum(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 8
        self.push_test(
            params = (7,[1,1,5,1,2,2,1,3,3,2,5,2,1],),
            expects= 2
        )
        self.push_test(
            params = (12,[1,1,2,3],),
            expects= 0
        )
        self.push_test(
            params = (100,[]),
            expects= 0
        )

    def solution(self, s, nums):
        if not nums or len(nums) ==0 : return 0
        start = end = total = 0
        length = 1<<30
        n = len(nums)
        while end < n:
            while end < n and total < s:
                total += nums[end]
                end += 1
            while start < end and total >= s:
                total -= nums[start]
                start += 1
            length = min(length, end - start + 1)
        if length > n: length = 0
        return length