__author__ = 'Daoyuan'
from BaseSolution import *

class PermutationsII(BaseSolution):
    """
    Given a collection of numbers that might contain duplicates, return all possible unique permutations.

    For example,
    [1,1,2] have the following unique permutations:
    [1,1,2], [1,2,1], and [2,1,1].
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,1,2],),
            expects = [[1,1,2],[1,2,1],[2,1,1]],
            expect_unordered = True
        )
        self.push_test(
            params = ([1,1],),
            expects = [[1,1]]
        )
        self.push_test(
            params = ([1,3,1,1],),
            expects = [[1,3,1,1],[1,1,1,3],[1,1,3,1],[3,1,1,1]],
            expect_unordered = True
        )

    def solution(self, nums):
        self.length = len(nums)
        self.result = []
        if not self.length : return self.result
        self.permutation(nums,0)
        #self.result = list(set(self.result))
        return self.result

    def unique(self, nums):
        seq = set()
        for idx,item in enumerate(nums):
            if item not in seq:
                seq.add(item)
                yield idx

    def permutation(self, nums, start):
        if start == self.length:
            self.result.append(nums)
            return
        for idx in self.unique( nums[start : self.length] ):
            arr = nums[:]
            if idx + start == start or arr[idx + start] != arr[start]:
                arr.insert(start, arr.pop( idx + start))
                self.permutation(arr, start + 1)