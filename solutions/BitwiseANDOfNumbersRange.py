from BaseSolution import *
class BitwiseANDOfNumbersRange(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (5,7),
            expect_oneof=4
        )
        self.push_test(
            params = (1,1),
            expects = 1
        )
        self.push_test(
            params= (3,4),
            expects = 0
        )
    def solution(self, m, n):
        import math
        if m == n: return m&n
        i = int(math.log(n-m, 2))
        return (0x7fffffff ^ (1<<i+1) -1 ) & m & n