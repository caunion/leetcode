from BaseSolution import *
class EvaluateReversePolishNotation(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (["10","6","9","3","+","-11","*","/","*","17","+","5","+"],),
            expects = 22
        )
        self.push_test(
            params = (["4", "13", "5", "/", "+"],),
            expects = 6
        )
    def solution(self, tokens):
        stack = []
        for token in tokens:
            if token[-1].isdigit():
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                ret = 0
                if token == "+":
                    ret = op1 + op2
                elif token == "-":
                    ret = op1 - op2
                elif token == "*":
                    ret = op1 * op2
                elif token == "/":
                    sign = -1 if op1 * op2 < 0 else 1
                    ret = abs(op1) / abs(op2) * sign
                stack.append(ret)
        return stack[0]