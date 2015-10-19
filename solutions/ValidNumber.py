__author__ = 'Daoyuan'
from BaseSolution import *

class ValidNumber(BaseSolution):
    """
    https://leetcode.com/problems/valid-number/

    Hard
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(("6e6.5",), False)
        self.push_test(
            params = (" -.01e+2093 ",),
            expects = True
        )
        self.push_test(
            params = ("  +123.569e.1 ",),
            expects = False
        )
        self.push_test(
            params = (" 2.e+1-.3 ",),
            expects = False
        )
        self.push_test( (" 2e ",), False)
        self.push_test( (" 2.3e.",), False)
        self.push_test( (" 2.3e1",), True)
        self.push_test( (" 2.3.e.",), False)


    def solution(self,s):
        beforeMius = True
        beforePeriod = True
        beforeE = True
        numBegin = False
        begin = True
        # String like "1.2f" is regarded invalid number by leetcode.
        # Under other case turn on this option
        allowSuffixF= False
        idx = 0
        s = s.strip()
        length = len(s)
        while idx < length:
            if s[idx] == '-' or s[idx] == '+':
                if beforeMius and begin:
                    begin = False
                    beforeMius = False
                    idx = idx + 1
                    continue
                else:
                    return False

            begin = False

            if (s[idx] == 'e' or s[idx] == 'E'):
                if beforeE and numBegin:
                    beforeMius= True
                    begin = True
                    beforeE = False
                    numBegin = False
                    beforePeriod= False
                    idx = idx + 1
                    continue
                else:
                    return False

            if s[idx]=='.':
                if beforePeriod:
                    beforePeriod = False
                    idx = idx + 1
                    continue
                else:
                    return False

            if idx == length - 1:
                if allowSuffixF and (s[idx] == 'f' or s[idx] == 'F'):
                    idx = idx + 1
                    continue

            if ord(s[idx]) >= 48 and ord(s[idx]) <= 57:
                numBegin = True
                idx = idx + 1
                continue
            else:
                return False
        else:
            if not numBegin:
                return False

        return True
