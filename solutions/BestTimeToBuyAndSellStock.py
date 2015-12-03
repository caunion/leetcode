__author__ = 'Daoyuan'
from BaseSolution import *
class BestTimeToBuyAndSellStock(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,6,3,2,5,6,7,8,9,9,4,3,1,4,5,7,8,5,4,3,5,4,3,2,4],),
            expects = 8
        )

    def solution(self, prices):
        if not prices or prices == [] : return 0
        n = len(prices)
        low = high = prices[0]
        lowp = highp = 0
        ret = 0
        for i in range(1, n):
            if prices[i] > high:
                high = prices[i]
                highp = i
            elif prices[i] < low:
                low = prices[i]
                lowp = i
            if lowp < highp:
                ret = max(ret, high - low)
            else:
                highp = lowp
                high = low
        return ret

    #DP way
    # s[i] denotes the maximum profit at i-th day.
    # then for s[i+1], s[i+1] = max(s[i], price[i+1] - min_so_far)

    def solution(self, prices):
        if not prices or prices == []: return 0
        n = len(prices)
        s = [0] * n
        min_so_far = prices[0]
        ret = 0
        for i in range(1, n):
            s[i] = max(s[i-1], prices[i] - min_so_far)
            min_so_far = min(min_so_far, prices[i])
        return s[n-1]