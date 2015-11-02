__author__ = 'Daoyuan'
from BaseSolution import *

class minstack(object):
    data = []
    minVal = []

    def __init__(self):
        self.data = []
        self.minVal = []

    def push(self, x):
        if self.top() is None:
            self.minVal.append(x)
            self.minVal.append(-1)
            self.data.append(x)
            return

        count, top = self.minVal[-1], self.minVal[-2]
        if top > x:
            self.minVal.append(x)
            self.minVal.append(-1)
        else:
            self.minVal[-1] = self.minVal[-1] - 1
        self.data.append(x)

    def pop(self):
        if self.top() is not None:
            self.data.pop()
            self.minVal[-1] = self.minVal[-1] + 1
            if not self.minVal[-1]:
                self.minVal.pop()
                self.minVal.pop()


    def top(self):
        if len(self.data) > 0: return self.data[-1]
        else: return None

    def getMin(self):
        if self.top() is not None:
            return self.minVal[-2]
        else:
            return None

class MinStack(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([2,1,2,3,4,1,1,0,2,2,1,2,3],),
            expects = [2,1,1,1,1,1,1,0,0,0,0,0,0,
                       0,0,0,0,0,1,1,1,1,1,1,2, None]
        )
    def solution(self, arr):
        stack = minstack()
        ret =[]
        for i in arr:
            stack.push(i)
            ret.append(stack.getMin())
        while stack.top() is not None:
            stack.pop()
            ret.append(stack.getMin())
        return ret