__author__ = 'Daoyuan'
from BaseSolution import *
class BestTimeToBuyAndSellStockIII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 8
        self.push_test(
            params = ([1,6,3,2,5,6,7,8,9,9,4,3,1,4,5,7,8,5,4,3,5,4,3,2,4],),
        )
    def solution(self, prices):
        if not prices or prices == [] or len(prices) == 1:
            return 0
        n = len(prices)
        ret = 0
        low = []
        for i in range(0, n-1): # to avoid TLE
            if prices[i] < prices[i+1]:
                low.append(i)

        for i in low:
            ret = max(ret, self.MaxProfit(prices, 0, i)+ self.MaxProfit(prices, i, n-1))
        return ret

    def MaxProfit(self, prices, left, right):
        if left == right: return 0
        high = low = prices[left]
        highp = lowp = left
        ret = 0
        for i in range(left+1, right+1):
            if prices[i] > high:
                high = prices[i]
                highp = i
            if prices[i] < low:
                low = prices[i]
                lowp = i
            if lowp < highp:
                ret = max(ret, high - low)
            elif highp < lowp:
                highp = lowp
                high = low
        return ret

    def solution(self, prices):
        if not prices or len(prices) < 2: return 0
        n = len(prices)
        s = [[0] * n for i in xrange(3)]
        for i in range(1,3):
            localMax = s[i-1][0] - prices[0]
            for j in range(1, n):
                s[i][j] = max(s[i][j], s[i][j-1], localMax + prices[j])
                localMax = max(localMax, s[i-1][j] - prices[j])
        return s[2][-1]