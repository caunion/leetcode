__author__ = 'Daoyuan'
from BaseSolution import *
class HouseRobberII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ([2,7,7,7,4],),
            expects = 11
        )
    def solution(self, nums):
        if not nums  or nums == []:return 0
        n = len(nums)
        ret = nums[0]
        if n == 1: return ret

        ret = max(nums[0], nums[1])
        if n == 2: return ret

        ret = max(nums[0],nums[1],nums[2])
        if n == 3: return ret

        ret = max(nums[0] + self.dp(nums, 2, n-2), self.dp(nums, 1, n-3) + nums[n-1], self.dp(nums, 0, n-2))
        return ret

    def dp(self, nums, left, right):
        if left == right:
            return nums[left]
        elif left + 1 == right:
            return max(nums[left], nums[right])
        else:
            n = len(nums)
            s = [0] * n
            s[left] = nums[left]
            s[left+1] = max(nums[left], nums[left+1])
            s[left+2] = max(nums[left], nums[left+1], nums[left+2])
            for i in range(left + 2, right+1):
                s[i] = max(s[i-1], s[i-2]+nums[i])
            return s[right]