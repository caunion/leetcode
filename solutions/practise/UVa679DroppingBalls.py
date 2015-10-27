__author__ = 'Daoyuan'

from ..BaseSolution import *

class UVa679DroppingBalls(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ([
                [1,3],
                [3,8],
                [3,2],
                [4,2],
                [10, 1],
                [2, 2],
                [8, 128],
                [16, 12345]
                     ],),
            expects = [
                1,
                7,
                6,
                12,
                512,
                3,
                255,
                36358
            ]
        )

    def solution(self, params):
        result = []
        for param in params:
            deep, idx = param[0], param[1]
            ret = 1
            tmp = 0
            while deep > 1:
                if idx % 2 == 0:
                    ret = ret * 2 + 1
                    idx = idx / 2
                else:
                    ret = ret * 2
                    idx = idx /2 + 1
                deep = deep -1
            result.append(ret)
        return result