__author__ = 'Daoyuan'
from BaseSolution import *

class PerfectSquares(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, n):
        squares = []
        for i in range(1, n):
            square = i * i
            if square > n:
                break
            else:
                squares.append(square)
        length = len(squares)
        count = 1e9
        for i in range(length-1, max(length /2 -1, -1), -1 ):
            number = n

            #for j in range(i, -1, -1):

    def find_min_sqaures(self, squares, num):
            pass