__author__ = 'Daoyuan'
from BaseSolution import *
class ValidParentheses(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("()[]{}",),
            expects = True
        )
        self.push_test(
            params = ("(){[()]{}}",),
            expects = True
        )
        self.push_test(
            params = ("()[{]}",),
            expects = False
        )

    def solution(self, s):
        stack = []
        if len(s) == 0: return False
        for c in s:
            stack.append(c)
            if len(stack) < 2: continue
            while len(stack) >=2:
                top1, top2 = stack[-2], stack[-1]
                if self.match(top1,top2):
                    stack.pop()
                    stack.pop()
                else:
                    break
        return len(stack) == 0

    def match(self, left, right):
        if left == "(" and right == ")" or\
                left == "[" and right == "]" or\
                left == "{" and right == "}":
            return True
        return False