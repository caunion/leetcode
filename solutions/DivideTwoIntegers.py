from BaseSolution import *
class DivideTwoIntegers(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (-2147483648,-1),
            expects = 2147483648
        )
    def solution(self, dividend, divisor):
        inf = (1<<30) + (1<<30) -1
        if divisor == 0:
            return -1
        else:
            d = dividend
            f = divisor
            ret = 0
            if d >= 0 and f > 0 or d<=0 and f<0:
                sign = 1
            else:
                sign = -1
            d, f = abs(d), abs(f)
            while d - f > 0:
                d -= f
                ret +=1
            ret *= sign

            return ret