__author__ = 'Daoyuan'
from BaseSolution import *
class Permutations(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,2,3],),
            expects = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
            expect_unordered=True
        )
        self.push_test(
            params = ([1,2],),
            expects = [[1,2],[2,1]]
        )
        self.push_test(
            params = ([2],),
            expects = [[2]]
        )
        self.push_test(
            params = ([],),
            expects = []
        )
        self.push_test(
            params = ([1,2,3,4],),
        )

    def solution(self, nums):
        self.length = len(nums)
        if not self.length: return []
        self.result  = []
        self.permutation_lexico_order(nums, 0)
        return self.result

    def permutation_lexico_order(self,nums,start):
        if start == self.length:
            self.result.append(nums)
            return
        for i in range(start, self.length):
            arr = nums[:]
            arr.insert(start, arr.pop(i))
            self.permutation_lexico_order(arr, start + 1)

    def permutation(self, nums, start):
        if start == self.length:
            self.result.append(nums)
            return
        for i in range(start, self.length):
            arr = nums[:]
            arr[start], arr[i] = arr[i], arr[start]
            self.permutation(arr,start+1)
