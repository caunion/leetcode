from BaseSolution import *
class GasStation(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([5],[4],),
            expects = -1
        )
        self.push_test(
            params = ([1,2,3,4,5],[4,3,2,1,5]),
            expects=  2
        )

    def solution(self, gas, cost):
        if not gas or not cost: return -1
        if sum(gas) < sum(cost): return -1
        n = len(gas)
        start = 0
        i = 0
        end = n-1
        count = 0
        tank = 0
        while count <= 2*n:
            if i == end:
                return start
            tank += gas[i]
            if tank < cost[i]:
                end = i
                start = (i+1) % n
                tank = 0
            else:
                tank -= cost[i]
            i = (i+1)%n
            count += 1
        return  -1 # will not reach here