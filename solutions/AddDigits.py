__author__ = 'Daoyuan'

from BaseSolution import *

class AddDigits(BaseSolution):
    """
    https://leetcode.com/problems/add-digits/
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (38,),
            expects = 2
        )


    def solution(self, num):
        if num == 0:
            return 0
        elif num % 9 ==0:
            return 9
        return num % 9