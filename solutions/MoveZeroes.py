__author__ = 'Daoyuan'
from BaseSolution import *
class MoveZeroes(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([0,0,1],),
        )
    def solution(self, nums):
        if nums:
            i = count= 0
            while i < len(nums) and count < len(nums):
                if nums[i] == 0:
                    nums.append(0)
                    nums.pop(i)
                else:
                    i+=1
                count+=1