__author__ = 'Daoyuan'

from ..BaseSolution import *

class UVa572OilDeposits(BaseSolution):
    """
    Array-like graph DFS: FloodFill
    p.259
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([
                "1 1",
                "*",
                "3 5",
                "*@*@*",
                "**@**",
                "*@*@*",
                "1 8",
                "@@****@*",
                "5 5",
                "****@",
                "*@@*@",
                "*@**@",
                "@@@*@",
                "@@**@",
                "0 0"
            ],),
            expects = [0,1,2,2]
        )

    def solution(self, params):
        idx = 0
        result = []
        while True:
            self.n,self.m= (int(item) for item in params[idx].split(" "))
            if self.n==0 and self.m==0:
                break
            self.index = [[0] * self.m for i in xrange(self.n)]
            self.pic = [ params[i] for i in range(idx+1, idx+self.n+1)]
            id = 0
            for i in xrange(self.n):
                for j in xrange(self.m):
                    if self.pic[i][j] == "@" and self.index[i][j] ==0:
                        id = id + 1
                        self.dfs(i,j,id)
            idx = idx + self.n + 1
            result.append(id)
        return  result

    def dfs(self, x, y, id):
        if x < 0 or x >= self.n or y < 0 or y >= self.m: return
        if self.index[x][y] > 0 or self.pic[x][y] == '*': return #if accessed or not deposit, return
        self.index[x][y] = id
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i==j==0: continue
                self.dfs(x+i,y+j, id)
        return
