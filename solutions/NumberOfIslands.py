__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *

class NumberOfIslands(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([
                "11110",
                "11010",
                "11000",
                "00000"
                ],),
            expects = 1
        )
        self.push_test(
            params = ([
                "11000",
                "11000",
                "00100",
                "00011"
                ],),
            expects = 3
        )

    def solution(self, grid):
        if len(grid) == 0: return 0
        n,m = len(grid), len(grid[0])
        self.n, self.m = n,m
        self.mat = [ [ grid[i][j] == "1"  for j in xrange(m) ] for i in xrange(n) ]
        count = 0
        for i in xrange(n):
            for j in xrange(m):
                if self.dfs(i,j): count+=1
        return count

    def dfs(self, i,j):
        if not self.mat[i][j]: return False
        else:
            self.mat[i][j] = False
            if i+1<self.n: self.dfs(i + 1 , j )
            if i-1>=0: self.dfs( i-1, j)
            if j+1<self.m: self.dfs( i, j+1)
            if j-1>=0: self.dfs( i, j-1)
            return True