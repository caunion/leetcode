__author__ = 'Daoyuan'
from BaseSolution import *

class Combinations(BaseSolution):
    """
    Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

    For example,
    If n = 4 and k = 2, a solution is:
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (4,2,),
            expects = [
                      [2,4],
                      [3,4],
                      [2,3],
                      [1,2],
                      [1,3],
                      [1,4],
                    ],
            expect_unordered=True
        )
        self.push_test(
            params = (2,1),
            expects = [[1],[2]],
            expect_unordered=True
        )
        self.push_test(
            params = (1,2),
            expects = [[1]]
        )
        self.push_test(
            params = (0,2),
            expects = []
        )


    def solution(self, n, k):
        if n <= 0: return []
        k = min(self.factory(n), k)
        nums = range(1,n+1)
        self.result = []
        self.combination(nums, k, 0)
        return self.result

    def combination(self, nums, k, idx):
        if k == 0:
            self.result.append( nums[0:idx] )
            return
        if len(nums) < k or len(nums) <= idx : return
        arr  = nums[:]
        arr.pop(idx)
        self.combination(arr, k, idx)
        arr = nums[:]
        self.combination(arr, k - 1, idx + 1)

    def factory(self, n):
        ret = 1
        while n > 1:
            ret = ret * n
            n = n -1
        return ret