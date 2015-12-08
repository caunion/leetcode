from BaseSolution import *
class FindMinimumInRotatedSortedArrayII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,1,1,1,1,1,0,1,1,1],),
            expects = 0
        )
    def solution(self, nums):
        if not nums or len(nums) == 0: return -1
        if len(nums) == 1: return nums[0]
        n = len(nums)
        j = self.findLeastLarge(nums, 0, n-1)
        return nums[j]

    def findLeastLarge(self, nums, left, right):
        mid = ( left + right ) /2
        n = len(nums)
        if left == right:
            return left
        elif nums[mid] > nums[right]:
            return self.findLeastLarge(nums, mid+1, right)
        elif nums[mid] < nums[right]:
            return self.findLeastLarge(nums, left, mid)
        else:
            p1 = self.findLeastLarge(nums, left, mid)
            p2 = self.findLeastLarge(nums, mid+1, right)
            if nums[p1] < nums[p1-1]:
                return p1
            else:
                return p2