__author__ = 'Daoyuan'
from BaseSolution import *

class IsomorphicStrings(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("egg", "bee"),
            expects = True
        )
        self.push_test(
            params = ("title","paper"),
            expects = True
        )
        self.push_test(
            params = ("dog","lol"),
            expects = False
        )

    def solution(self, s, t):
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}
        for a, b in zip(s,t):
            if map1.has_key(a) != map2.has_key(b):
                return False
            if map1.has_key(a) == False:
                map1[a] = b
                map2[b] = a
            elif map1[a] != b or map2[b] != a:
                return False
        return True