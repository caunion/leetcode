__author__ = 'Daoyuan'

from ..BaseSolution import BaseSolution

class BoxInALine(BaseSolution):
    """

    E.g. 6.5, p231
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ([
                [4,2],
                [4],
                [4]
                     ],),
            expects= 4
        )
        self.push_test(
            params= ([
                [6,4],
                [1,1,4],
                [4],
                [4],
                [2,3,5]
                     ],),
            expects= 9
        )
        self.push_test(
            params= ([
                [6,6],
                [1,1,4],
                [2,3,5],
                [4],
                [4],
                [3,1,6],
                [4]
                     ],),
            expects= 12
        )
        self.push_test(
            params= ([
                [6,3],
                [1,1,4],
                [2,3,5],
                [3,1,6]
                     ],),
            expects= 9
        )
        self.push_test(
            params = ([
                [6,3],
                [1,1,4],
                [2,3,5],
                [3,1,6]
                    ],),
            expects = 9
        )

        self.push_test(
            params= ([
                [100000,1],
                [4],
                [4],
                [4]
                     ],),
            expects = 2500050000
        )

    def link(self, left, right, L, R):
        right[L] = R
        left[R] = L

    def swap(self, a, b):
        tmp = a
        a = b
        b = tmp
        return (a,b)

    def solution(self, param):
        n = param[0][0]
        m = param[0][1]
        left = range(-1, n)
        right = range(1,n+2)
        s = range(0, n+1) # box value
        left[0] = n
        right[n] = 0
        for i in range(1, m+1):
            opt = param[i][0]
            if opt == 4:
                left, right = self.swap(left, right)
            else:
                L = param[i][1]
                R = param[i][2]
                LX, LY = left[L], right[L]
                RX, RY = left[R], right[R]
                if opt == 3:
                    self.link(left, right, LX, R)
                    self.link(left, right, R, LY)
                    self.link(left, right, RX,L)
                    self.link(left, right, L, RY)
                elif opt == 2:
                    self.link(left, right, LX, LY)
                    self.link(left, right, L, RY)
                    self.link(left, right, R, L)
                elif opt == 1:
                    self.link(left, right, LX, LY)
                    self.link(left, right, RX, L)
                    self.link(left, right, L, R)

        sum = 0
        last = 0
        for i in range(0, n, 1):
            last = right[last]
            if i % 2 == 0:
                sum = sum + last
        return sum
