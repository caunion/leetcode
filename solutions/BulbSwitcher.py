from BaseSolution import *
class BulbSwitcher(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (10, ),
            expects= 3
        )

    # Only complete square number has odd divisors. i.e. 9 {1,3,9}, 8 {1,2,4,8}
    def solution(self, n):
        import math
        return int(math.sqrt(n))