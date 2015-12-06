__author__ = 'Daoyuan'
from ..BaseSolution import *
class KMP(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("bbcabbca","bbbssssbbcabbcabbcacabbcabbca"),
            expects = [7,11,21]
        )
    def solution(self, p, s):
        return self.kmp(p,s)

    def computePrefixFunc(self, p):
        n = len(p)
        f = [0] * (n+1)
        f[0] = 0
        f[1] = 0
        for i in xrange(1,n):
            k = f[i]
            while k and p[k] != p[i]:
                k = f[k]
            if p[k] == p[i]:
                k += 1
            f[i+1] = k
        return f

    def kmp(self, p, s):
        f = self.computePrefixFunc(p)
        n = len(s)
        m = len(p)
        k = 0
        ret = []
        for i in xrange(0, n):
            while k>=m or k > 0 and p[k] != s[i]:
                k = f[k]
            if p[k] == s[i]:
                k += 1
            if k == m:
                ret.append(i - m+1)
        return ret

