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
        self.fuckinglevel = 8
        self.push_test(
            params = (3,3),
            expects = [[1,2,3]],
            expect_unordered=True
        )
        self.push_test(
            params = (2,2),
            expects = [[1,2]],
            expect_unordered=True
        )
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
        return list(self.combines(nums, k, 0))

    def combines(self, nums, k, idx):
        for i in range(idx, len(nums)):
            if k == 1:
                yield [nums[i]]
            else:
                for next in  self.combines(nums, k-1, i+1):
                    yield [nums[i],] + next

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

    ## other's solution with iteration
    ## DFS
    def solution(self, n, k):
        res, stack=[], [([i for i in xrange(1,n+1)], k, [])]
        while stack:
            lst, k, temp=stack.pop()
            if k<=len(lst):
                if not k:
                    res+=temp,
                for i in xrange(len(lst)):
                    stack+=(lst[i+1:],k-1,temp+[lst[i]]),
        return res



    ## combination is essentially BFS a tree.
    ## so does permutation.
    ## so, the it can be write as either a recursion or a iteration
    def solution(self, n, k):
        k = min(n, k)
        nums = range(1,n+1)
        return self.bfs( range(1,n+1), k)

    def bfs(self, nums, k):
        queue = [ (i, k, [ nums[i],])  for i in xrange(len(nums))] #nodes at root layer
        ret = []
        length = len(nums)
        while len(queue) > 0:
            top = queue.pop(0)
            if top[1] == 1:
                ret.append( top[2] )
            else:
                for j in range(top[0] + 1, length):
                    queue.append( (j, top[1]-1, top[2] + [ nums[j],]) ) # extend child node to queue
        return ret
