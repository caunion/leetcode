__author__ = 'Daoyuan'
from BaseSolution import *
class SearchInsertPosition(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,2,3],-1),
            expects= 0
        )
    def solution(self, nums, target):
        if not nums or len(nums) == 0: return 0
        n = len(nums)
        return self.findMostSmall(nums, target, 0, n-1)

    def findMostSmall(self, nums, target, left, right):
        mid = (left + right) /2
        if left==right:
            if nums[left] >= target:
                return left
            else:
                return left + 1
        elif nums[mid] >= target:
            return self.findMostSmall(nums, target, left, mid)
        else:
            return self.findMostSmall(nums, target, mid+1, right)