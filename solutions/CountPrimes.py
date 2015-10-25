__author__ = 'Daoyuan'

from BaseSolution import *

class CountPrimes(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test((2,),0)
        self.push_test((10,),4)
        self.push_test((1,),0)
        self.push_test((499979,))
        self.push_test((99992 ,))
        self.push_test((99989,))

    def solution(self, n):
        if n<=0: return 0
        table = [True] * (n+2)
        table[0] = False
        table[1] = False
        table[2] = True
        lim = int(self.sqrt(n))
        for i in range(2, lim+1):
            if table[i] == False:
                continue
            for j in range( i*i, n,i):
                if j >= n: break
                table[j] = False
        count =0
        for i in range(2, n):
            if table[i]:
                count = count+1
        return  count
    def sqrt(self, num):
        if num==0:
            return  0
        precision = 1.0
        x1 = x0 = num/2.0
        while True:
            x1 = 0.5 * (x0 + num / (x0 * 1.0) )
            if abs(x0 -x1 )< precision:
                break
            else:
                x0 = x1
        return x1
