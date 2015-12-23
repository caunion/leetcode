from BaseSolution import *
class ReverseInteger(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (0, ),
            expects= 0
        )
        self.push_test(
            params = (-1000000009, ),
            expects= 0
        )
        self.push_test(
            params = (-123, ),
            expects= -321
        )

    def solution(self, x):
        if x < 0: sign = -1
        else: sign = 1
        ret = str(abs(x))
        ret = ret[::-1]
        if int(ret) > 0x7fffffff and sign > 0 or \
           int(ret) > 0x80000000 and sign < 0: return 0
        return sign * int(ret)