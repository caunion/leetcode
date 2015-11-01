__author__ = 'Daoyuan'
from BaseSolution import *
class NextPermutation(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,2,3,4],),
            expects = [1,2,4,3]
        )
        self.push_test(
            params = ([1,4,3,2],),
            expects = [2,1,3,4]
        )
        self.push_test(
            params = ([1,5,1,1],),
            expects = [5,1,1,1]
        )
        self.push_test(
            params = ([4,3,2,1],),
            expects = [1,2,3,4]
        )
        self.push_test(
            params = ([1],),
            expects = [1]
        )
        self.push_test(
            params = ([],),
            expects = []
        )

    def solution(self, nums):
        lst = nums[:]
        self.inplace_solve(lst)
        return lst

    def inplace_solve(self, nums):
        length = len(nums)
        i = length-1
        if i <= 0: return

        last = nums[i]
        while i > 0:
            if nums[i-1] >= last:
                last = nums[i-1]
                i = i-1
            else:
                break

        j = length - 1
        i = i - 1
        if i < 0: # 4,3,2,1
            nums.reverse()
            return
        # 1,3,4,2
        while j > i:
            if nums[j] > nums[i]:
                break
            else:
                j = j -1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = sorted(nums[i+1:])
        return