from BaseSolution import *
class LargestRectangleInHistogram(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        self.push_test(
            params = ([2,1,2],),
            expects = 3
        )
    def solution(self,height):
        if not height or len(height) == 0: return 0
        height.append(0)
        height.insert(0,0)
        n = len(height)
        stack = []
        ans = 0
        for i in range(0, n):
            if len(stack) == 0 or height[i] > height[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and height[stack[-1]] > height[i]:
                    top = stack.pop()
                    left = stack[-1] if len(stack) > 0 else -1
                    ans = max(ans, height[top] * (i - left- 1))
                stack.append(i)
        return ans
