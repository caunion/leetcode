from BaseSolution import *
class FindMinimumInRotatedSortedArray(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([7,8,9,10,11,12,3,4,5],),
            expects = 3
        )
    def solution(self, nums):
        if not nums or len(nums) == 0: return -1
        if len(nums) == 1: return nums[0]
        n = len(nums)
        return self.findLeastLarge(nums, 0, n-1)

    def findLeastLarge(self, nums, left, right):
        mid = ( left + right ) /2
        n = len(nums)
        if left == right:
            return nums[left]
        elif nums[mid] > nums[right]:
            return self.findLeastLarge(nums, mid+1, right)
        else:
            return self.findLeastLarge(nums, left, mid)