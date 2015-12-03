__author__ = 'Daoyuan'
from BaseSolution import *
class BestTimeToBuyAndSellStockIV(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        self.push_test(
            params = (2,[1,7,4,2]),
            expects = 6
        )
        self.push_test(
            params = (7,[1,2,3,4,4,3,23,4,4,5,4,3,1,2,3,4,2,3,4,5,6,7,5,4,3,5,6,7,8,9,4,3,5,6,3,5,76,8,6,5,4,2,2,4,6,7,8,6,5,3,2,21,32,4,5,6,4,3,2,2,4,4,5,67,87,6,5,4,3,2,5],),
            expects = 228
        )
        self.push_test(
            params = (4,[1,2,3,4,4,3,23,4,4,5,4,3,1,2,3,4],),
            expects = 27
        )

    ## Buggy version!!!!!!
    ## cut lowest transactions ( cut minimal (high[i] - low[i]) ) each time
    ## what if 2 transaction result the same income, we should choose the lowest one to shrink,
    ## which will results in O(n^3)...
    def solution(self, k, prices):
        if not prices or prices == [] or len(prices) == 1: return 0
        n = len(prices)
        low = []
        high = []
        i = 0
        while i < n-1:
            for i in range(i, n-1):
                if prices[i] < prices[i+1]:
                    low.append(i)
                    break
            for i in range(i, n-1):
                if prices[i] > prices[i+1]:
                    high.append(i)
                    break
            if i == n - 2:
                if len(low) == 0: return 0
                if prices[low[-1]] < prices[i+1]:
                    high.append(n-1)
                break

        l = len(low)
        k = min(l, k)
        for i in range(0, l - k):
            lp = -1
            lowProfit = 1<<30
            for i in xrange(len(low)):
                if prices[high[i]] - prices[low[i]] < lowProfit:
                    lowProfit = prices[high[i]] - prices[low[i]]
                    lp = i
            if 0<lp<len(low)-1 and prices[low[lp]] < prices[low[lp+1]] and prices[high[lp]] > prices[high[lp-1]]:
                if prices[high[lp]] - prices[high[lp-1]] > prices[low[lp+1]] - prices[low[lp]]:
                    high[lp-1] = high[lp]
                else:
                    low[lp+1] = low[lp]
            elif lp < len(low) -1 and prices[low[lp]] < prices[low[lp+1]]:
                low[lp+1] = low[lp]
            elif lp > 0 and  prices[high[lp]] > prices[high[lp-1]]:
                high[lp-1] = high[lp]
            low.pop(lp)
            high.pop(lp)

        ret = 0
        for i in range(0, len(low)):
            ret+= prices[high[i]] - prices[low[i]]
        return ret

    def solution(self, k, prices):
        if not prices or prices == [] or len(prices) == 0:
            return 0
        n = len(prices)
        if k > n/2:
            ret = 0
            for i in range(0, n-1):
                ret += max(prices[i+1] - prices[i] ,0)
            return ret
        s = [ [0] * (n) for i in xrange(k+1)]
        for i in range(1, k+1):
            localMax = s[i-1][0] - prices[0]
            for j in range(1, n):
                    s[i][j] = max(s[i][j], s[i][j-1], prices[j] + localMax)
                    localMax = max(localMax, s[i-1][j] - prices[j])
        return s[k][n-1]

