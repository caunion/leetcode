__author__ = 'Daoyuan'
from BaseSolution import *

nums = [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0]
def isBadVersion(n):
    return nums[n-1] == 0

class FirstBadVersion(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = [len(nums),],
            expects = 12
        )

    def solution(self, n):
        return self.firstBadSearch(1,n)

    def firstBadSearch(self, left, right):
        m = (left + right) / 2
        if left == right:
            if isBadVersion(left):
                return left
            else:
                return -1
        elif isBadVersion(m):
            return self.firstBadSearch(left, m)
        else:
            return self.firstBadSearch(m+1,right)
