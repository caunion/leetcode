__author__ = 'Daoyuan'
from ..BaseSolution import *
class BinaryIndexedTree(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([15,14,13,12,11,10,9,8,7,6,5,4,3,2,1], [(7,7), (0,2), (7,14), (-1<<30, 1, 2),(-1<<30, 7, 3),(7,7),(0,2), (7,14)]),
            expects = [8,42,36,3,30,31]
        )
    def solution(self, nums, query):
        self.buildTrree(nums)
        result = []
        for q in query:
            if len(q) == 2:
                l,r = q
                ret = self.query(l,r)
                result.append(ret)
            else:
                _, p, v =q
                self.update(p,v)
        return result

    def buildTrree(self, nums):
        n = len(nums)
        self.nums =nums
        self.c = [0] * (n+1)
        self.n = n
        for i, num in enumerate(nums):
            self.add(i, num)
        return

    def query(self,left, right):
        return self.sum(right) - self.sum(left-1)
    def lowbit(self,x):
        return x&-x
    def sum(self, x):
        x+=1
        ret = 0
        while x > 0:
            ret += self.c[x]
            x -= self.lowbit(x)
        return ret
    def add(self, x, v):
        x+=1
        while x<= self.n:
            self.c[x] += v
            x += self.lowbit(x)
    def update(self, x, v):
        add = v - self.nums[x]
        self.add(x, add)