__author__ = 'Daoyuan'
from ..BaseSolution import *
class LongestIncreaseSeq(BaseSolution):
    '''
    1st solution: use Longest Common Seq. assume input sequence as s, sort s to get s'
                  calculate lcs(s,s') to get longest increase seq O(n^2)
    2nd solution: this one. O(nlogn)
    '''
    def __init__(self):
        self.fuckinglevel = 9
        BaseSolution.__init__(self)
        self.push_test(
            params= ("15423526",),
            expects = ["12356"],
            expect_oneof= True
        )


    def solution(self, s):
        return self.lis(s)

    def lis(self, s):
        n = len(s)
        s = " " + s
        m = [-1] * (n+1)
        p = [-1] * (n+1)
        L = 0
        for i in range(1, n+1):
            j = self.binSearch(s,m,s[i],1,L)
            p[i] = m[j]
            if j == L or s[m[j+1]] > s[i]:
                m[j+1] = i
                L = max(L, j+1)
        # reconstruct result
        ret = ""
        position = m[L]
        for i in xrange(L):
            ret = s[position] + ret
            position = p[position]

        return ret
    def binSearch(self,s, m, x, left, end):
        if left > end:
            return 0
        if left == end: return left
        mid = (left + end) / 2
        if int(x) <= int(s[m[mid]]):
            return self.binSearch(s, m, x, left, mid)
        elif int(x) > int(s[m[mid+1]]):
            return self.binSearch(s, m, x, mid+1, end)
        else:
            return mid