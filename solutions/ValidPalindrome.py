__author__ = 'Daoyuan'
from BaseSolution import *

class ValidPalindrome(BaseSolution):
    """

    Easy
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (",.",),
            expects = True
        )
        self.push_test(
            params = ("A man, a plan, a canal: Panama",),
            expects = True
        )
        self.push_test(
            params = ("race a car",),
            expects = False
        )

    def solution(self, s):
        if s is None or len(s) == 0 or len(s) == 1:
            return True
        left =0
        length = len(s)
        right = length- 1
        while left <= right:
            while left <= right:
                code_left = ord(s[left])
                if code_left <= 90 and code_left >=65:
                    code_left  = code_left + 32
                    break
                elif code_left >=97 and code_left <=122:
                    break
                elif code_left <=57 and code_left >= 48:
                    break
                left =  left + 1
            if left >= right:
                break
            while left <= right:
                code_right = ord(s[right])
                if code_right<= 90 and code_right >=65:
                    code_right = code_right + 32
                    break
                elif code_right >= 97 and code_right <= 122:
                    break
                elif code_right <=57 and code_right >= 48:
                    break
                right = right -1
            left = left + 1
            right = right - 1
            if code_left != code_right:
                return False
        return  True

