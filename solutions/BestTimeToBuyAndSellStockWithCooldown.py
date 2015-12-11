__author__ = 'Daoyuan'
from BaseSolution import *
class BestTimeToBuyAndSellStockWithCooldown(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([6,1,3,2,4,7],),
            expects = 6
        )
    def solution(self, prices):
        if not prices or len(prices) <= 1: return 0
        n = len(prices)
        sell = [0] * n
        buy = [0] * n
        rest = [0] * n
        buy[0] = -prices[0]
        sell[0] = 0
        rest[0] = 0
        localmax =buy[0]
        for i in xrange(1, n):
            sell[i] = localmax + prices[i]
            buy[i] = rest[i-1] - prices[i]
            localmax = max(localmax, buy[i])
            rest[i] = max(sell[i-1], rest[i-1])
        return max(0, sell[n-1], rest[n-1])