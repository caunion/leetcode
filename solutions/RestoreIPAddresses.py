__author__ = 'Daoyuan'
from BaseSolution import *

class RestoreIPAddresses(BaseSolution):
    """
    Note: 01.0.01.0 is ILLEGAL.
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("010010",),
            expects = ["0.10.0.10","0.100.1.0"]
        )
        self.push_test(
            params = ("25525511135",),
            expects = ["255.255.11.135", "255.255.111.35"]
        )
        self.push_test(
            params = ("555555555555555",),
            expects = []
        )
        self.push_test(
            params = ("172162541",),
            expects =["17.216.25.41","17.216.254.1","172.16.25.41","172.16.254.1","172.162.5.41","172.162.54.1"]
        )

    def solution(self, s):
        ret = list( self.combine(s, 4, "") )
        return ret

    def combine(self, s, k, prefix):
        if len(prefix) > 0: sep = "."
        else: sep = ""
        for i in xrange(1,4):
            if k == 1:
                seg = s
            else:
                seg = s[0:i]
            if len(s) / (k*1.0) > 3 or \
                        len(s) / (k*1.0) < 1 or \
                        int(seg)>255 or\
                        len(seg) > 1 and seg[0] == "0":  #pruning
                return
            if k == 1:
                yield prefix + sep + s
            else:
                prev = "" # remove dupe
                for next in self.combine( s[i:], k - 1, prefix + sep + seg):
                    if next==prev: continue
                    prev =next
                    yield next