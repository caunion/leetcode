__author__ = 'Daoyuan'
from BaseSolution import *
class DecodeWays(BaseSolution):
    '''
    Be careful with the boundary condition
    The key for this question is to write down the
    state transition function.
    '''
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("11012209",),
            expects = 2
        )
        self.push_test(
            params = ("1232212322",),
            expects = 48
        )
    def solution(self, s):
        if not s or s == "": return 0
        n = len(s)
        c = [0] * (n+1)
        if int(s[0]) == 0:
            return 0
        else:
            c[0] = 1

        if n == 1: return c[0]

        if int(s[1]) == 0:
            if int(s[0:2]) > 26:
                return 0
            else:
                c[1] = 1
        else:
            if int(s[0:2]) > 26:
                c[1] = 1
            else:
                c[1] = 2

        for j in range(2, n):
            if int(s[j]) != 0 and int(s[j-1]) != 0:
                if int(s[j-1:j+1]) > 26:
                    c[j] = c[j-1]
                else:
                    c[j] = c[j-1] + c[j-2]
            elif int(s[j]) == 0 and int(s[j-1]) != 0:
                 if int(s[j-1:j+1]) <= 26:
                     c[j] = c[j-2]
                 else:
                    return 0
            elif int(s[j]) == 0 and int(s[j-1]) == 0:
                return 0
            else:
                c[j] = c[j-1]

        return c[n-1]