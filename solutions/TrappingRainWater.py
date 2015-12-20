__author__ = 'Daoyuan'
from BaseSolution import *

class TrappingRainWater(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([0,1,0,2,1,0,1,3,2,1,2,1],),
            expects = 6
        )

    def solution(self, height):
        if not height or len(height) < 2: return 0
        stack = []
        ret = 0
        n = len(height)
        for i in range(0, n):
            if len(stack) == 0 or height[stack[-1]] > height[i]:
                stack.append(i)
            elif height[stack[-1]] == height[i]:
                stack.pop()
                stack.append(i)
            else:
                while len(stack) > 0 and height[stack[-1]] < height[i]:
                    top = stack.pop()
                    if len(stack) > 0:
                        h = (min(height[stack[-1]], height[i]) - height[top] )
                        w = (i - stack[-1] - 1)
                        ret += (h*w)
                stack.append(i)
        return ret

    # beautiful drain method
    # introduced by https://leetcode.com/discuss/62506/easy-to-understand-python-10-line-60ms-o-n
    def solution(self, height):
        if not height or len(height) < 2: return 0
        n = len(height)
        waterLevel = [0] * n
        left = right = 0
        for i,h in enumerate(height):
            left = max(h, left)
            waterLevel[i] = left

        for i in xrange(n-1, -1, -1):
            h = height[i]
            right = max(right, h)
            waterLevel[i] = min(waterLevel[i], right) - h
        ret = sum(waterLevel)
        return ret