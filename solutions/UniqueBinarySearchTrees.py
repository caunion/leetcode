__author__ = 'Daoyuan'
from BaseSolution import *

class UniqueBinarySearchTrees(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (10,),
            expects = 16796
        )
        self.push_test(
            params = (4,),
            expects = 14
        )

    def solution(self, n):
        if not hasattr(self, "ret"):
            self.ret = [1,1,2,5]
        self.solve(n)
        return self.ret[n]

    def solve(self, n):
        if n < len(self.ret):
            return self.ret[n]
        result = 0
        for left in xrange(n):
            right = n -1 - left
            num = self.solve(left)
            num = num * self.solve(right)
            result += num
        self.ret.append(result)
        return result