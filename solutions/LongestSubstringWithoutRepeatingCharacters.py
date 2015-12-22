from BaseSolution import *
class LongestSubstringWithoutRepeatingCharacters(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("abac",),
            expects= 3
        )
        self.push_test(
            params = ("",),
            expects= 0
        )
        self.push_test(
            params = ("aaaaa",),
            expects= 1
        )
        self.push_test(
            params = ("acaaaad",),
            expects= 2
        )
        self.push_test(
            params = ("acacefafcedaad",),
            expects= 5
        )
    def solution(self, s):
        if not s or len(s) == 0: return 0
        inf = 1<<30
        p1 = [inf] * 97
        ret = 0
        for i,c in enumerate(s):
            p = self.char2num(c)
            if p1[p] < inf:
                ret = max(i - min(p1), ret)
                for j in xrange(0, 97):
                    if p1[j] < p1[p]:
                        p1[j] = inf
            p1[p] = i
        ret = max(ret, i+1 - min(p1))
        return ret

    # a better solution
    def solution(self, s):
        if not s or len(s) == 0: return 0
        inf = 1<< 30
        start = 0
        p1 = [inf] * 130
        ret = 0
        for i,c in enumerate(s):
            p = self.char2num(c)
            if start > p1[p]:
                p1[p] = inf
            if p1[p] < inf:
                start = p1[p] + 1
            p1[p] = i
            ret = max(ret, i - start + 1)
        return ret
    def char2num(self, c):
        return ord(c) - ord('a')