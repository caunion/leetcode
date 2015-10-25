__author__ = 'Daoyuan'
from BaseSolution import *

class UglyNumber(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test((25,), True)
        self.push_test((-2**31,), False)
        self.push_test((14,), False)
        self.push_test((24,), True)
        self.push_test((32,), True)

    def solution(self, num):
        if num == 1: return True
        if num <= 0: return False
        while True:
            flag = False
            if num % 2 == 0:
                num = num / 2
                flag = True
            if num % 3 == 0:
                num = num / 3
                flag = True
            if num % 5 == 0:
                num = num / 5
                flag = True
            if num == 1:
                return True
            if not flag:
                if num != 0:
                    return False