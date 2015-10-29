__author__ = 'Daoyuan'

from ..BaseSolution import *

class UVa699TheFallingLeaves(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([
                "5 7 -1 6 -1 -1 3 -1 -1",
                "8 2 9 -1 -1 6 5 -1 -1 12 -1 -1 3 7 -1 -1 -1"
            ],),
            expects = [
                [7, 11, 3],
                [9,7,21,15]
            ]
        )

    def solution(self, params):
        result = []
        for param in params:
            numbers = [int(i) for i in param.split(" ")]
            buf = [0] * (len(numbers) + 1)
            self.solve(numbers, [0], buf, 0)
            right = []
            left = []
            reverse = False
            for i in buf:
                if i == 0:
                    reverse = True
                    continue
                if not reverse:
                    right.append(i)
                else:
                    left.append(i)
            left.extend(right)
            result.append(left)
        return result

    def solve(self, numbers, idx, buf, idxbuf):
        cur = idx[0]
        if numbers[cur] < 0:
            return
        buf[ idxbuf ] = buf[idxbuf] + numbers[cur]
        idx[0] = idx[0] + 1
        left = numbers[idx[0]]
        if  left > 0: # left child
            self.solve(numbers, idx, buf, (idxbuf - 1 + len(buf) ) % len(buf) )
        idx[0] = idx[0] + 1
        right=numbers[idx[0]]
        if right > 0: # right child
            self.solve(numbers, idx, buf, (idxbuf + 1 + len(buf) ) % len(buf) )
        return