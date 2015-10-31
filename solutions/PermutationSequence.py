__author__ = 'Daoyuan'
from BaseSolution import *

class PermutationSequence(BaseSolution):

    """
    Very Brain-burn for Boundary Conditions

    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        self.push_test(
            params = (3, 6),
            expects = "321"
        )
        self.push_test(
            params = (3, 3),
            expects = "213"
        )
        self.push_test(
            params = (9, 3),
            expects = "123456879"
        )
        self.push_test(
            params = (9, 6),
            expects = "123456987"
        )
        self.push_test(
            params = (9, 24),
            expects = "123459876"
        )
        self.push_test(
            params = (9, 25),
            expects = "123465789"
        )

    def solution(self, n, k):
        numbers = range(n, 0, -1)
        factories = range(1,n+1)
        for i in range(2, n):
            factories[i] = factories[i] * factories[i-1]

        while True:
            if k == 0 or k == 1:
                break
            for i in xrange(len(factories)):
                if k <= factories[i]:
                    break
            for j in xrange(1, i+1+1):
                if k <= factories[i - 1] * j:
                    break
            left = i
            right = i- j + 1
            numbers.insert(left,numbers.pop(right))
            k = k - factories[i -1] * (j-1)

        numbers.reverse()
        return "".join([str(item) for item in numbers ])