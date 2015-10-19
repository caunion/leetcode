__author__ = 'Daoyuan'

from BaseSolution import *

class ReverseWordsInAString(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("",),
            expects = ""
        )
        self.push_test(
            params = ("      ",),
            expects = ""
        )
        self.push_test(
            params = ("  the  sky   is blue",),
            expects = "blue is sky the"
        )

    def solution(self, s):
        segs = s.split(" ")
        segs.reverse()
        segs = [seg for seg in segs if len(seg) > 0]
        if len(segs) == 0: return ""
        ret = reduce(lambda a,b: a + ' '+b, segs )
        return ret.strip()
