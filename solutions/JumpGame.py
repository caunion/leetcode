from BaseSolution import *
class JumpGame(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([3,2,0,1,1,4,2,1,0,4],),
            expects= True
        )
        self.push_test(
            params = ([3,2,1,1,0,1,1,4,2,1,0,4],),
            expects= False
        )

    def solution(self, nums):
        if not nums or len(nums) < 2: return True
        n = len(nums)
        i = n - 2
        dist = 1
        while i >= 0:
            while nums[i] < dist and i >= 0:
                i -= 1
                dist +=1

            if i == 0:
                return nums[i] >= dist
            elif i < 0:
                return False
            else:
                dist = 1
                i -= 1

    def canJump(self, nums):
        if not nums or len(nums) < 2 : return True
        n = len(nums)
        farest = 0
        for i, d in enumerate(nums):
            if i == n-1 or farest < i: break
            farest = max(farest, i + d)
        return farest >= n-1 