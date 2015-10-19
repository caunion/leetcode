__author__ = 'Daoyuan'

from BaseSolution import *

class PalindromeNumber(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (121,),
            expects = True
        )
        self.push_test(
            params = (0,),
            expects = True
        )
        self.push_test(
            params = (211,),
            expects = False
        )
    def solution(self, x):
        return str(x)[::-1] == str(x)