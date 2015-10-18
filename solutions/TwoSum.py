__author__ = 'Daoyuan'
from BaseSolution import *

class TwoSum(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ([150,24,79,50,88,345,3],200),
            expects = [1,4]
        )
        self.push_test(
            params= ([-1,-2,-3,-4,-5], -8),
            expects= [3,5]
        )
        self.push_test(
            params= ([2,7,11,15], 9),
            expects= [1,2]
        )

    def solution (self, nums, target):
        length = len(nums)
        idx = sorted( range(0,length), key= lambda s : nums[s])
        left = 0; right = idx[length-1]
        while True:
            leftnum = nums[idx[left]]; rightnum = nums[idx[right]]
            if leftnum + rightnum == target:
                if idx[left] <= idx[right]:
                    return [ idx[left]+1, idx[right]+1]
                else:
                    return [ idx[right]+1, idx[left]+1]
            elif leftnum + rightnum < target:
                left = left+1
            else:
                right = right-1
        return [-1,-1]

    def solution_back(self, nums, target):
        length = len(str(target))
        hashtable = []
        for i in range(0,length):
            subtable = []
            hashtable.append(subtable)
            for j in range(0,10):
                subtable.append(set())

        combination = [
                        [[0,0],[1,9],[2,8],[3,7],[4,6],[5,5]],
                        [[0,1],[2,9],[3,8],[4,7],[5,6]],
                        [[0,2],[1,1],[3,9],[4,8],[5,7],[6,6]],
                        [[0,3],[1,2],[4,9],[5,8],[6,7]],
                        [[0,4],[1,3],[2,2],[5,9],[6,8],[7,7]],
                        [[0,5],[1,4],[2,3],[6,9],[7,8]],
                        [[0,6],[1,5],[2,4],[3,3],[7,9],[8,8]]
                        [[0,7],[1,6],[2,5],[3,4],[8,9]]
                        [[0,8],[1,7],[2,6],[3,5],[4,4],[9,9]]
                        [[0,9],[1,8],[2,7],[3,6],[4,5]]
                    ]
        for idx in len(nums):
            itemstr = str( nums(idx) )
            for i, j in zip(range(0, len(itemstr)),range(len(itemstr)-1, -1, -1)):
                num = int(itemstr[j])
                hashtable[i][num].add(idx)

        strtar = str(target)

        resultset1 = set()
        resultset2 = set()
        for i,j in zip(range(0,length), range(length-1, -1, -1)):
            digit = strtar[j]
            table = hashtable[i]
            pass
        # THINK TOO MUCH