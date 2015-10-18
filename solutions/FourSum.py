__author__ = 'Daoyuan'

from BaseSolution import *

class FourSum(BaseSolution):
    """
    Given an array S of n integers, are there elements a, b, c, and d in S
    such that a + b + c + d = target? Find all unique quadruplets in the
    array which gives the sum of target.

    :url: https://leetcode.com/problems/4sum/
    :time: 10 min
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ([1,0,-1,0,-2,2],0),
            expects = [ [-1,  0, 0, 1], [-2, -1, 1, 2], [-2,  0, 0, 2] ],
            expect_unordered = True
        )

    def solution(self, nums, target):
        length = len(nums)
        nums = sorted(nums)

        result = set()
        for i in xrange(length):
            first = nums[i]
            for j in range(i+1, length):
                second = nums[j]
                left = j + 1
                right = length -1
                if left >= right:
                    break
                while True:
                    if left >= right:
                        break
                    cursor = first + second + nums[left] + nums[right]
                    if cursor == target:
                        result.add( (first, second, nums[left], nums[right]))
                        left = left+1
                    elif cursor > target:
                        right = right -1
                    else:
                        left = left + 1

        result = [ list(item) for item in result]
        return result