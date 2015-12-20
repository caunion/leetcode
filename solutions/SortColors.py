from BaseSolution import *
class SortColors(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([0,1,2,2,1,1,1,1,2,2,2,2,1,1,1,1,1,0],),
            expects= [0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2]
        )
    def solution(self, nums):
        self.sortColors(nums)
        return nums
    def sortColors(self, nums):
        if not nums or len(nums) == 0: return
        n = len(nums)
        count = [0]*3
        for num in nums:
            count[num]+=1
        for i in xrange(n):
            for color in [0,1,2]:
                if count[color] > 0:
                    nums[i] = color
                    count[color] -= 1
                    break
        return