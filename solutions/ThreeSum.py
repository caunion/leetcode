__author__ = 'Daoyuan'
from BaseSolution import *

class ThreeSum(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([0],),
            expects = []
        )
        self.push_test(
            params = ([-1,0,1,2,-1,-4], ),
            expects = [[-1, 0, 1],[-1, -1, 2]],
            expect_unordered = True
        )
        self.push_test(
            params= ([0,7,-4,-7,0,14,-6,-4,-12,11,4,9,7,4,-10,8,10,5,4,14,6,0,-9,5,6,6,-11,1,-8,-1,2,-1,13,5,-1,-2,4,9,9,-1,-3,-1,-7,11,10,-2,-4,5,10,-15,-4,-6,-8,2,14,13,-7,11,-9,-8,-13,0,-1,-15,-10,13,-2,1,-1,-15,7,3,-9,7,-1,-14,-10,2,6,8,-6,-12,-13,1,-3,8,-9,-2,4,-2,-3,6,5,11,6,11,10,12,-11,-14], )

        )


    def solution(self,nums):
        target = 0
        length = len(nums)
        idx = sorted( range(0, length), key= lambda s: nums[s])
        result = set()
        for i in xrange(length):
            current = nums[ idx[i] ]
            left = i+1
            right = length-1
            if current > 0 or right <= left:
                break
            while True:
                if right == left:
                    break
                cursor = current + nums[ idx[left] ] + nums[ idx[right] ]
                if cursor == target:
                    result.add( (current, nums[ idx[left]], nums[idx[right]]) )
                    left = left+1
                elif cursor>target:
                    right = right - 1
                else:
                    left = left + 1

        result = [list(item) for item in result]
        return result

