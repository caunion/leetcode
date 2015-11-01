__author__ = 'Daoyuan'
from BaseSolution import *

class GenerateParentheses(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (3,),
            expects = [
                "((()))",
                "(()())",
                "()(())",
                "(())()",
                "()()()"
            ],
            expect_unordered = True
        )
        self.push_test(
            params = (1,),
            expects = [
                "()"
            ],
            expect_unordered = True
        )
        self.push_test(
            params = (0,),
            expects = [],
            expect_unordered = True
        )
        self.push_test(
            params = (8,),
            expect_unordered = True
        )

    def solution(self, n):
        if n == 0: return []
        ret = sorted(list(set(self.insert("()", n-1))))
        return ret

    def insert(self, prev, n):
        if n == 0:
            yield prev
        else:
            for i in range(len(prev) + 1):
                for item in self.insert(prev[0:i] +  "()" + prev[i:], n-1):
                    yield item

