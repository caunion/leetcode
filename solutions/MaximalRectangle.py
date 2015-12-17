__author__ = 'Daoyuan'
from BaseSolution import *
class MaximalRectangle(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        self.push_test(
            params=(["10","10"],),
            expects = 2
        )
        self.push_test(
            params = (["101001110","111000001","001100011","011001001","110110010","011111101","101110010","111010001","011110010","100111000"],),
            expects = 6
        )
        self.push_test(
            params = (["10111","01010","11011","11011","01111"],),
            expects = 6
        )
        self.push_test(
            params = (["0110010101","0010101010","1000010110","0111111010","0011111110","1101011110","0001100010","1101100111","0101101011"],),
            expects = 10
        )

        self.push_test(
            params = (["0001","1101","1111","0111","0111"],),
            expects = 9
        )
        self.push_test(
            params=(['10100','10111','11111','10010'],),
            expects = 6
        )
    def solution(self, matrix):
        if not matrix or matrix == [] : return 0
        n = len(matrix)
        m = len(matrix[0])
        h = [[0] * m for i in xrange(n)]
        w = [[0] * m for i in xrange(n)]
        s = [[0] * m for i in xrange(n)]
        s[0][0] = h[0][0] = w[0][0] = 1 if int(matrix[0][0]) == 1 else 0
        for i in xrange(1,n):
            if int(matrix[i][0]) == 1:
                h[i][0] = h[i-1][0] + 1
                w[i][0] = 1
                s[i][0] = s[i-1][0] + 1
        for j in xrange(1,m):
            if int(matrix[0][j]) == 1:
                h[0][j] = 1
                w[0][j] = w[0][j-1] + 1
                s[0][j] = s[0][j-1] + 1
        for i in xrange(1,n):
            for j in xrange(1, m):
                if int(matrix[i][j]) == 1:
                    h[i][j] = 1
                    w[i][j] = 1
                    s[i][j] = 1
                    if int(matrix[i-1][j]) == 1:
                        h[i][j] = max(h[i][j], h[i-1][j] + 1)
                        s[i][j] = max(h[i][j]*1,s[i][j])
                    if int(matrix[i][j-1]) == 1:
                        w[i][j] = max(w[i][j], w[i][j-1] + 1)
                        s[i][j] = max(1*w[i][j],s[i][j])
                    if int(matrix[i-1][j-1]) == 1:
                        if min(h[i-1][j-1] + 1, h[i-1][j] + 1) * min(w[i-1][j-1] + 1, w[i][j-1] + 1) >= s[i][j]:
                            h[i][j] = min(h[i-1][j-1] + 1, h[i-1][j] + 1)
                            w[i][j] = min(w[i-1][j-1] + 1, w[i][j-1] + 1)
                            s[i][j] = h[i][j] * w[i][j]

        ret = max([s[i][j] for j in xrange(m) for i in xrange(n)])
        return ret

    def solution(self, matrix):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return 0
        n = len(matrix)
        m = len(matrix[0])
        h = [[0]*(m+1) for i in xrange(n)]
        ans = 0
        for i in xrange(0, n):
            stack = []
            for j in range(0, m+1):
                if j == m:
                    h[i][j] =0
                elif int(matrix[i][j]) == 1:
                    if i == 0:
                        h[i][j] = 1
                    else:
                        h[i][j] = h[i-1][j] + 1

                if len(stack)==0 or h[i][stack[-1]] <h[i][j]:
                    stack.append(j)
                else:
                    while len(stack) > 0 and h[i][stack[-1]] > h[i][j]:
                        top = stack.pop()
                        if len(stack) > 0:
                            ans = max(ans, (j-stack[-1] -1) * h[i][top])
                        else:
                            ans = max(ans, j *  h[i][top])
                    stack.append(j)
        return ans