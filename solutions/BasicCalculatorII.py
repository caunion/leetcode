from BaseSolution import *
class BasicCalculatorII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("1+2*3+4*5/2-6",),
            expects= 11
        )
        self.push_test(
            params = ("0 + 1-2+3*4 / 2 -12 + 3 * 4",),
            expects= 5
        )
    def solution(self,s):
        if not s or len(s) == 0: return -1
        s += "#"
        number, oprand =  [], []
        add = set(["+", "-"])
        mul = set(["*", "/"])
        num = 0
        for c in s:
            needShrink = False
            sign = 0
            if c.isdigit():
                num = num*10 + int(c)
            elif c in mul:
                number.append(num)
                num = 0
                if len(oprand) > 0 and 3 <=oprand[-1] <= "4":
                    prev = oprand.pop()
                    op1 = number.pop()
                    if prev == 3:
                        number[-1] = number[-1] * op1
                    elif prev ==4:
                        number[-1] = number[-1] / op1
                if c == "*":
                    sign = 3
                elif c=="/":
                    sign = 4
            elif c in add:
                number.append(num)
                num = 0
                if len(oprand) > 0 and oprand[-1] != 5:
                    needShrink = True
                if c == "+":
                    sign = 1
                elif c == "-":
                    sign = 2
            elif c == "#":
                number.append(num)
                num = 0
                needShrink = True
            while needShrink and len(oprand) > 0 and 1<=oprand[-1] <=4:
                    prev = oprand.pop()
                    op1 = number.pop()
                    if prev == 1:
                        number[-1] = number[-1] + op1
                    elif prev ==2:
                        number[-1] = number[-1] - op1
                    elif prev == 3:
                        number[-1] = number[-1] * op1
                    elif prev ==4:
                        number[-1] = number[-1] / op1
            if sign:
                oprand.append(sign)
        return number[0]