from ..BaseSolution import *
class UVa12563(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (3,10, [2,7,8],),
            expects = (3, 687)
        )
        self.push_test(
            params = (3,100, [60,70,80],),
            expects = (2, 758)
        )
        self.push_test(
            params = (3, 100, [30, 69, 70],),
            expects = (3, 777)
        )

    def solution(self, n, t, songs):
        if n == 0 or t == 0: return (0,0)
        d = [[0]*(1+t) for i in xrange(n)]
        time = [[0]*(1+t) for i in xrange(n)]
        for j in range(1, t+1):
            if j > songs[0]:
                d[0][j] = 1
                time[0][j] = songs[0]
        for i in xrange(1, n):
            for j in xrange(1, t+1):
                if j > songs[i]:
                    d[i][j] = max(d[i-1][j],d[i-1][j-songs[i]] + 1)
                    time[i][j] = max(time[i-1][j], time[i][j-songs[i]] + songs[i] )
                else:
                    d[i][j] = max(d[i][j], d[i-1][j])
                    time[i][j] = max(time[i][j], time[i-1][j])
        return (d[n-1][t] + 1, time[n-1][t] + 678)

    def solution(self, n, t, songs):
        if n==0 or t==0: return (0,0)
        d = [0]*(1+t)
        time = [0]*(1+t)
        for j in range(1, t+1):
            if j > songs[0]:
                d[j] = 1
                time[j] = songs[0]
        for i in range(1,n):
            for j in (t,0,-1):
                if j > songs[i]:
                    d[j] = max(d[j], d[j-songs[i]]+1)
                    time[j] = max(time[j], time[j-songs[i]]+songs[i])
        return (d[t]+1,time[t]+678)


