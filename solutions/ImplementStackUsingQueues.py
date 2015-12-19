from BaseSolution import *

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = []
        self.inf = 1<<32

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.insert(0, x)

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.empty():
            q2 = []
            while len(self.q1)> 1:
                last = self.q1.pop()
                q2.insert(0, last)
            last = self.q1.pop()
            self.q1 = q2
            return last
        else:
            return self.inf

    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            top = self.pop()
            self.push(top)
            return top
        else:
            return self.inf


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) == 0

## CONSTANT OPERATION
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        self.inf = 1<<31
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.q) > 0:
            queue = [x]
            queue.insert(0, self.q)
            self.q = queue
        else:
            self.q.insert(0, x)

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.empty():
            last = self.q.pop()
            if len(self.q) > 0:
                remains = self.q.pop()
                self.q = remains
            return last
        else:
            return self.inf

    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.q[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0


class ImplementStackUsingQueues(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ([ [3], [0, 1], [0, 2], [2], [1],[3], [1], [3]],),
            expects=[True, None, None, 2, 2,False, 1, True]
        )
    def solution(self, oprations):
        stack = Stack()
        result = []
        for op in oprations:
            if op[0] == 0:
                result += stack.push(op[1]),
            elif op[0] == 1:
                result += stack.pop(),
            elif op[0] == 2:
                result += stack.top(),
            elif op[0] == 3:
                result += stack.empty(),
        return result