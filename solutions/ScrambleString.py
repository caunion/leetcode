from BaseSolution import *
class ScrambleString(BaseSolution):
    """
    Pay attention to the DP solution. The way of caching a middle value
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        self.push_test(
            params = ("abb","bba"),
            expects = True
        )
        self.push_test(
            params = ("abcd","dcba"),
            expects= True
        )
        self.push_test(
            params = ("abcd","bdac"),
            expects= False
        )

    # non-DP version
    # Leetcode testcase might be too weak
    def solution(self, s1, s2):
        return self.isScrambleNonDP(s1,s2)
    def isScrambleNonDP(self, s1,s2):
        n = len(s1)
        if len(s1) != len(s2): return False
        if s1 == s2: return True
        dic1 = {}
        dic2 = {}
        for i in xrange(len(s1)):
            c,d = s1[i], s2[i]
            if c not in dic1:
                dic1[c] = 0
            else:
                dic1[c] += 1
            if d not in dic2:
                dic2[d] = 0
            else:
                dic2[d] += 1
        for c in s2:
            if c not in dic1 or dic1[c] != dic2[c]:
                return False
        for k in xrange(1, n):
            if self.isScrambleNonDP(s1[0:k], s2[0:k]) and self.isScrambleNonDP(s1[k: n], s2[k : n]):
                return True
            if self.isScrambleNonDP(s1[0:k], s2[n-k: n]) and self.isScrambleNonDP(s1[k:n], s2[0: n-k]):
                return True
        return False


    def solution(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        n, m = len(s1), len(s2)
        self.cache = {}
        return self.isScrambleDP(0, n, 0, m)

    def isScrambleDP(self, l1, r1, l2, r2):
        key = "%d_%d#%d_%d" %(l1,r1,l2,r2)
        ret = None
        if key in self.cache:
            return self.cache[key]
        if r1-l1 != r2 - l2:
            return False
        if self.s1[l1:r1] == self.s2[l2:r2]:
            ret = True
        if ret is None:
            dic1 = {}
            dic2 = {}
            for i,j in zip(range(l1, r1), range(l2,r2)):
                c,d = self.s1[i], self.s2[j]
                if c not in dic1:
                    dic1[c] = 0
                else:
                    dic1[c] += 1
                if d not in dic2:
                    dic2[d] = 0
                else:
                    dic2[d] += 1
            for i in range(l2,r2):
                c = self.s2[i]
                if c not in dic1 or dic1[c] != dic2[c]:
                    ret = False
        if ret is None:
            for k in range(1, r1-l1):
                if self.isScrambleDP(l1,l1+k, l2, l2+k) and self.isScrambleDP(l1+k, r1, l2+k, r2):
                    ret = True
                    break
                if self.isScrambleDP(l1, l1+k, r2-k, r2) and self.isScrambleDP(l1+k, r1, l2, r2-k):
                    ret = True
                    break
        if ret is None:
            ret = False
        self.cache[key] = ret
        return ret
