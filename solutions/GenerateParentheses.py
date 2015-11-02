__author__ = 'Daoyuan'
from BaseSolution import *

class GenerateParentheses(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 8
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

    ## TLE method. brutal
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

    def solution(self, n):
        if n == 0: return []
        self.result = []
        self.generate(0,0,"", n)
        return self.result

    ## non-yield top-down method. Save top result in parameters and pass it to the child node (recursion tree)
    def generate(self, left, right, s, n):
        if left == n and left == right:
            self.result.append(s)
            return
        if left < n:
            self.generate(left+1, right, s+"(", n)
        if left > right:
            self.generate(left, right+1, s + ")", n)
        return

    def solution(self, n):
        if n == 0: return []
        ret = list(self.generate_yield(0,0,n))
        return ret

    ## yield is bottom-up. Like I just append a value of this step "(" or ")" to the result from child
    def generate_yield(self, left, right, n):
        if left == right == n:
            yield ""
            return
        if left < n:
            for next in self.generate_yield(left+1, right, n):
                yield "(" + next
        if left > right:
            for next in self.generate_yield(left, right+1, n):
                yield ")" + next

    def solution(self, n):
        if n == 0: return []
        return list(self.generate_yield_top_down(0,0,"", n) )

    ## mixed yield and top-down.. quick ugly..
    def generate_yield_top_down(self, left, right,s, n):
        if left == right == n:
            yield s
            return
        if left < n:
            for next in self.generate_yield_top_down(left + 1, right, s+"(", n):
                yield next
        if left > right:
            for next in self.generate_yield_top_down(left, right + 1, s + ")", n):
                yield  next