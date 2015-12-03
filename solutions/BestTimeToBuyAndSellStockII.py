__author__ = 'Daoyuan'
from BaseSolution import *
class BestTimeToBuyAndSellStockII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([2,1],),
            expects = 0
        )
        self.push_test(
            params = ([1,6,3,2,5,6,7,8,9,9,4,3,1,4,5,7,8,5,4,3,5,4,3,2,4],),
            expects = 23
        )
    def solution(self, prices):
        if not prices or prices == []:
            return 0
        n = len(prices)
        if n == 1: return 0
        low= high = i= ret= 0
        while i < n-1:
            for low in range(i, n-1):
                if prices[low] < prices[low+1]:
                    break
            i = low
            for high in range(i, n-1):
                if prices[high] > prices[high+1]:
                    break
            i = high
            if low < high:
                ret += prices[high] - prices[low]
            elif i == n-2:
                ret += max(0, prices[n-1] - prices[low])
                break
        return ret