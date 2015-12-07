__author__ = 'Daoyuan'
from BaseSolution import *
class ReverseBits(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (43261596,),
            expects = 964176192
        )
    def solution(self, n):
        if not hasattr(self,'table'):
            self.genTable()
        num = n
        b1 = num & (255)
        b2 = (num & (255<<8))>>8
        b3 = (num & (255<<16))>>16
        b4 = (num & (255<<24))>>24
        ret = (self.table[b4] << 0) + (self.table[b3] << 8) + (self.table[b2]<<16) + (self.table[b1]<<24)
        return ret
    def genTable(self):
        self.table = [0] * (1<<8)
        for num in xrange(1<<8):
            ret = 0
            for i in range(0,8):
                ret += ((num & (1<<i)) >> i)
                if i < 7: ret = ret << 1
            self.table[num] = ret
        return