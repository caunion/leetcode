__author__ = 'Daoyuan'
from BaseSolution import *
class AddBinary(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("11","1",),
            expects = "100"
        )

    def solution(self, a, b):
        return bin( int(a,2) + int(b,2))[2:]