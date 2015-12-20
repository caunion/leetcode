from BaseSolution import *
class ContainerWithMostWater(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([5,2,12,1,5,3,4,11,9,4],),
            expects = 55
        )
        self.push_test(
            params = ([2,3,10,5,7,8,9],),
            expects= 36
        )

    def solution(self, height):
        ans = -1
        if not height or len(height) < 2: return 0
        n = len(height)
        left = 0
        right = n - 1
        while left < right:
            ans = max(ans, min(height[right], height[left]) * (right - left) )
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return ans