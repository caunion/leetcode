__author__ = 'Daoyuan'
from BaseSolution import *
class SearchForARange(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 8
        self.push_test(
            params = ([1,2,2,3,3,4,4,4,4,4,4,5,5,5,5,5,6,6,6], 4),
            expects = [5, 10]
        )
        self.push_test(
            params = ([1,2,3,4], 0),
            expects = [-1, -1]
        )
        self.push_test(
            params = ([1], 2),
            expects = [-1, -1]
        )
        self.push_test(
            params = ([1,1,1,1,1,2,2,2,2], 3),
            expects = [-1, -1]
        )
        self.push_test(
            params = ([1,1,1,1,1,2,2,2,2], 2),
            expects = [5, 8]
        )
    def solution(self, nums, target):
        if not nums or nums == []: return [-1, -1]
        nums.insert(0, -1<<30)
        nums.append(1<<30)
        n = len(nums)
        left = self.findMostSmall(nums, target, 0, n-1)
        right = self.findLeastLarge(nums, target, 0, n-1)
        left = max(left, -1)
        right = min(right, n-1)
        return [left - 1, right-1]
    def findLeastLarge(self, nums, target, left, right):
        mid = ( left + right) /2
        if left == right:
            if nums[left-1] == target:
                return left-1
            else:
                return 0
        elif left > right:
            return -1
        elif nums[mid] <= target:
            return self.findLeastLarge(nums, target, mid+1, right)
        else:
            return self.findLeastLarge(nums, target, left, mid)

    def findMostSmall(self, nums, target, left, right):
        mid = (left + right) /2 + (left + right) % 2
        if left == right:
            if nums[left+1] == target:
                return left+1
            else:
                return 0
        elif left > right:
            return  -1
        elif nums[mid] < target:
            return self.findMostSmall(nums, target, mid, right)
        else:
            return self.findMostSmall(nums, target, left, mid-1)