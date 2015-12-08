from BaseSolution import *
class MajorityElement(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, nums):
        if not nums or len(nums) == 0: return -1
        dic = {}
        length = len(nums)
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
            if dic[n] > length / 2:
                return n