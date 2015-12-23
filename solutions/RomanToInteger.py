from BaseSolution import *
class RomanToInteger(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("DCXIV",),
            expects = 614
        )
        self.push_test(
            params = ("MCMLIV",),
            expects= 1954
        )
    def solution(self, s):
        ret = 0
        map = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
        n = len(s)
        i = 0
        while i < n:
            tmp = 0
            while i + 1 < n and map[s[i]] == map[s[i+1]]:
                tmp += map[s[i]]
                i += 1
            if i + 1< n and map[s[i]] < map[s[i+1]]:
                tmp = map[s[i+1]] - map[s[i]] - tmp
                i += 2
            else:
                tmp += map[s[i]]
                i += 1
            ret += tmp
        return ret