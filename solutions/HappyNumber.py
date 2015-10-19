__author__ = 'Daoyuan'
from BaseSolution  import *

class HappyNumber(BaseSolution):
    """

    Write an algorithm to determine if a number is "happy". A
    Happy number like 19. 1^2 + 9^2=82, 8^2+2^2= 68, 6^2+8^2 =100,  1^2 + 0^2 + 0^2= 1

    Easy
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (19,),
            expects = True
        )
        self.push_test(
            params = (2,),
            expects = False
        )

    def solution(self, n):
        tmp = n
        path = set()
        while True:
            a = 0
            while tmp > 0:
                a = a + (tmp % 10)**2
                tmp = tmp / 10
            tmp = a

            if tmp == 1:
                return True
            else:
                if path.__contains__(tmp):
                    return False
                else:
                    path.add(tmp)
