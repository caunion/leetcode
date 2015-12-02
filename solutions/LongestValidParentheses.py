__author__ = 'Daoyuan'
from BaseSolution import *
class LongestValidParentheses(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        self.push_test(
            params = ("((()()())))(((())()()(",),
            expects = 10
        )
        self.push_test(
            params = ("()(())",),
            expects = 6
        )
        self.push_test(
            params = ("(()",),
            expects = 2
        )
        self.push_test(
            params = ("",),
            expects = 0
        )
        self.push_test(
            params = ("))()()))((()()((",),
            expects = 4
        )
    def solution2(self, s):
        s = " "+s
        n = len(s)
        p = range(0, n)
        for i in range(1, n):
            if s[ i-1 ] == "(" and s[i] == ")":
                p[i] = p[p[i-1]]
                if p[p[i] -1] < p[i] - 1:
                    p[i] = p[p[i]-1]
            elif s[ p[i-1]-1] == "(" and s[i] == ")":
                p[i] = p[p[i-1]-1]
                if p[p[i] -1] < p[i] - 1:
                    p[i] = p[p[i]-1]

        ret = max([  i - p[i] + 1 if i!=p[i] else 0 for i in range(1, n)])
        return ret

    ## O(n) time compexity, O(1) space
    ## note the use of 2 for, one from left to right and the other from right to left, to
    ## deal with the asymetery of parenthess. Such as '(()' and '())' will be the same thing.
    def solution(self, s):
        s = " " + s
        n = len(s)
        ret = 0
        tmp = 0
        pos = 1
        for i in range(1, n):
            tmp += 1 if s[i] == "(" else -1
            if tmp < 0:
                pos = i+1
                tmp = 0
            elif tmp == 0:
                ret = max(ret, i - pos + 1)
        pos = n-1
        tmp = 0
        for i in range(n-1, 0, -1):
            tmp += 1 if s[i] == ")" else -1
            if tmp < 0:
                pos = i-1
                tmp = 0
            elif tmp == 0:
                ret = max(ret, pos - i + 1)
        return ret