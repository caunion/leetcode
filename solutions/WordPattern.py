__author__ = 'Daoyuan'
from BaseSolution import *

class WordPattern(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ("abba","dog cat cat dog"),
            expects = True
        )
        self.push_test(
            params = ("abba", "dog, cat cat fish"),
            expects = False
        )

        self.push_test(
            params = ( "aaaa", "dog cat cat dog"),
            expects = False
        )

        self.push_test(
            params = ("abba","dog dog dog dog"),
            expects = False
        )

    def solution(self, pattern, str):
        segs = str.split(" ")

        if len(segs) != len(pattern):
            return False

        map1 = {}
        map2 = {}
        for p, seg in zip(pattern, segs):
            if map1.has_key(p) != map2.has_key(seg):
                return False

            if map1.has_key(p) == False:
                map1[p] = seg
                map2[seg] = p

            elif p != map2[seg] or seg != map1[p]:
                return False

        return True

