from BaseSolution import *
class HIndex(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,2,3,3,4,3,22,4,4,2,3,4,5,6,7,4,4,3,6,5,4,3,3],),
            expects = 5
        )
    def solution(self, citations):
        if not citations or len(citations) == 0: return 0
        n = len(citations)
        c = [0] * n
        nums = sorted(citations)
        for i in range(0, n):
            j = n - i - 1
            if i == 0:
                c[i] = 1 if nums[j] > 0 else 0
            elif nums[j] >= i + 1:
                c[i] = i + 1
            else:
                c[i] = c[i-1]
        return c[n-1]
