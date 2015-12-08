from BaseSolution import *
class SearchInRotatedSortedArray(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([7,8,9,1,2,3,4],3),
            expects = 5
        )
        self.push_test(
            params= ([2],3),
            expects = -1
        )

    def solution(self, nums ,target):
        if not nums or len(nums) == 0: return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1
        n = len(nums)
        j = self.findLeastLarge(nums, 0, n-1)
        pos1 = self.findTarget(nums, target, 0, j)
        pos2 = self.findTarget(nums, target, j, n-1)
        if pos1 >= 0: return pos1
        if pos2 >= 0: return pos2
        return  -1

    def findTarget(self, nums, target, left, right):
        mid = (left+right)/2
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1
        elif nums[mid] < target:
            return self.findTarget(nums, target, mid+1, right)
        else:
            return self.findTarget(nums, target, left, mid)

    def findLeastLarge(self, nums, left, right):
        mid = ( left + right ) /2
        n = len(nums)
        if left == right:
            return left
        elif nums[mid] > nums[right]:
            return self.findLeastLarge(nums, mid+1, right)
        else:
            return self.findLeastLarge(nums, left, mid)