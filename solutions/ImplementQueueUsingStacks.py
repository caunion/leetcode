from BaseSolution import *

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        if not self.empty():
            return self.s2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append( self.s1.pop() )
        if not self.empty():
            return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0 and len(self.s2) == 0
class ImplementQueueUsingStacks(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ([ [3], [0, 1], [0, 2], [2], [1],[3], [1], [3]],),
            expects=[True, None, None, 1, 1,False, 2, True]
        )
    def solution(self, oprations):
        stack = Queue()
        result = []
        for op in oprations:
            if op[0] == 0:
                result += stack.push(op[1]),
            elif op[0] == 1:
                result += stack.pop(),
            elif op[0] == 2:
                result += stack.peek(),
            elif op[0] == 3:
                result += stack.empty(),
        return result