__author__ = 'Daoyuan'
from BaseSolution import *
import math

class PerfectSquares(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        self.push_test(
            params = (9453,),
        )
        self.push_test(
            params = (9975,)
        )
        self.push_test(
            params = (7929,)
        )
        self.push_test(
            params = (6337,)
        )

        self.push_test(
            params = (12,),
            expects = 3
        )
        self.push_test(
            params = (13,),
            expects = 2
        )
        self.push_test(
            params = (4,),
            expects = 1
        )
        self.push_test(
            params = (0,),
            expects = 0
        )

    ### TLE.
    ### Combination + Pruning
    ### for future reference
    def solution(self, n):
        squares = []
        for i in range(1, n):
            square = i * i
            if square > n:
                break
            else:
                squares += square,

        squares.reverse()
        least = [999]
        list(self.combinesum( squares, n, 1, least))
        if least[0] > 900: return 0
        return least[0]

    def combinesum(self, squares, target, count, least):
        if count > least[0]: return
        for i in xrange(len(squares)):
            if target % squares[i] ==0:
                n = target / squares[i]
                count = count + n -1
                if count < least[0]:
                    least[0] = count
                yield [squares[i],] * n
            elif squares[i] > target:
                continue
            elif squares[i] < target:
                tar = target % squares[i]
                n = target / squares[i]
                arr = self.less_than(squares, tar)
                this  = [squares[i],] * n
                for next in self.combinesum(arr, tar, count + n, least):
                    yield next +  this

    def less_than(self, arr, num):
        length = len(arr)
        start = length - 1
        end  = 0
        while start - end > 1:
            mid = ( start + end ) / 2
            if arr[mid] > num:
                end  = mid
            elif arr[mid] < num:
                start = mid
            else:
                end = mid
                break;
        return arr[end:]


    ## Convert from Java DP
    def solution(self, n):
        if n==0: return 0
        squares = [0] * (n + 1)
        squares[1] = 1
        for i in xrange(2,n+1):
            squares[i] = 1e9
            for j in xrange(1,i):
                if j * j > i: break
                squares[i] = min(squares[i], squares[i-j*j])
            squares[i] =squares[i] + 1
        return squares[n]


    # This variable to store the middle result
    # and can be reused by different test cases!!!!
    numSquares = [0]
    def solution(self, n):
        length = len(self.numSquares)
        if n >= length:
            square = [ i**2 for i in xrange(1, int(math.sqrt(n)) + 1)]
            for i in xrange(length, n+1): # attention, start from length
                self.numSquares += min( [ 1+ self.numSquares[ i - item ] for item in square if item <= i ] ),
        return self.numSquares[n]