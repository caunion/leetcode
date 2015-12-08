from BaseSolution import *
class HIndexII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ([1,1,1,2,2,2,4,5,7,8,9],),
            expects = 4
        )
        self.push_test(
            params= ([0],),
            expects = 0
        )
    def solution(self, citations):
        if not citations or len(citations) == 0: return 0
        return self.findLeastLarge(citations, 0, len(citations) - 1)

    def findLeastLarge(self, nums, left, right):
        mid = (right + left) / 2
        h = len(nums) - mid
        if left == right:
            h = len(nums) - right
            if nums[left] >=  h:
                return h
            else:
                return h -1
        elif nums[mid] < h:
            return self.findLeastLarge(nums, mid+1, right)
        else:
            return self.findLeastLarge(nums,left, mid)