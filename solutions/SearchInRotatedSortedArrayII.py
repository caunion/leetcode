from BaseSolution import *
class SearchInRotatedSortedArrayII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,1,1,1,0,1,1], 0),
            expects = True
        )
        self.push_test(
            params =([1,1,1,1,1,1,1,2,2,2,0,1,1,1,1,1],0),
            expects = True
        )
    def solution(self, nums, target):
        if not nums or len(nums) == 0: return -1
        if len(nums) == 1: return True if nums[0] == target else False
        n = len(nums)
        j = self.findLeastLarge(nums, 0, n-1)
        pos1 = self.findTarget(nums, target, 0, j)
        pos2 = self.findTarget(nums, target, j, n-1)
        if pos1 >= 0: return True
        if pos2 >= 0: return True
        return False

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
        elif nums[mid] < nums[right]:
            return self.findLeastLarge(nums, left, mid)
        else:
            p1 = self.findLeastLarge(nums, left, mid)
            p2 = self.findLeastLarge(nums, mid+1, right)
            if nums[p1] < nums[p1-1]:
                return p1
            else:
                return p2