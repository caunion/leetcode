from BaseSolution import *
class ExcelSheetColumnNumber(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("ABC",),
            expects = 731
        )

    def solution(self, s):
        ret = 0
        for c in s:
            ret = ret * 26 + ord(c) - ord('A') + 1
        return ret