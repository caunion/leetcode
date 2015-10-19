__author__ = 'Daoyuan'

from BaseSolution import *

class StringToInteger(BaseSolution):
    """
    Implement atoi to convert a string to an integer.

    note the boundary check:
    # -2147483649, 2147483648, '2aaa'
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test((" -1 ",),-1)
        self.push_test((" 1-3 ",), 1)
        self.push_test(("  -0012a42",), -12)
        self.push_test(("+123 ",), 123)
        self.push_test(("-",), 0)
        self.push_test(("",), 0)

    def solution(self, str):
        isMinus = False
        beforeMinus = True
        numBegin = False
        idx = 0
        str = str.strip()
        length = len(str)
        number = 0
        while idx < length:
            if str[idx] == "+" or str[idx] == "-":
                if idx ==0 and beforeMinus:
                    if str[idx] == "-":
                        isMinus = True
                    beforeMinus = False
                    idx = idx + 1
                    continue
                else:
                    break

            if ord(str[idx]) >= 48 and ord(str[idx]) <= 57:
                number = number * 10 + int(str[idx])
                idx = idx + 1
                numBegin = True
                continue
            else:
                break
        else:
            if not numBegin:
                return 0

        if isMinus:
            number = - number
        if number > 2147483647:
            return 2147483647
        if number < -2147483648:
            return -2147483648
        return number
