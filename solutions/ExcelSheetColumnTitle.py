from BaseSolution import *
class ExcelSheetColumnTitle(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (26,),
            expects = "Z"
        )
        self.push_test(
            params = (52,),
            expects = "AZ"
        )
        self.push_test(
            params = (731,),
            expects = "ABC"
        )

    def solution(self, n):
        ret = ""
        n -= 1
        while n >= 0:
            ret += chr( n % 26 + ord('A'))
            n = n / 26 -1
        ret = ret[::-1]
        return ret