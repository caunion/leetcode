from BaseSolution import *
class JumpGameII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([4,3,2,1,0,2],),
            expects= -1
        )
        self.push_test(
            param = ([2,3,1,1,2],),
            expects= 2
        )
        self.push_test(
            params = ([2,3],),
            expects= 1
        )
        self.push_test(
                params = ([2,3,1,2,4,2,1,3,4,3,2],),
                expects= 4
        )
    def solution(self, nums):
        ##
        ## s[i] indicates farest location at step i
        if not nums or len(nums) < 2: return 0
        n = len(nums)
        s = [0] * (n+1)
        s[0] = nums[0]
        for i in range(0, min(s[0]+1, n)):
            s[1] = max(nums[i]+i, s[1])
        if s[0]>= n-1: return 1
        if s[1]>= n-1: return 2
        for i in xrange(2, n):
            if s[i-1] >= n-1:
                return i
            for j in range(s[i-2]+1, s[i-1] + 1):
                s[i] = max(s[i], nums[j] + j)
        return -1
