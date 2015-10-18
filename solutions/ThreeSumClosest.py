__author__ = 'Daoyuan'

from BaseSolution import *

class ThreeSumClosest(BaseSolution):
    """
    Given an array S of n integers, find three integers in S such that the sum is closest to a given number,
    target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    :url: https://leetcode.com/problems/3sum-closest/
    :time: about 15 min
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([30,-5,-84,76,65,-77,50,9,-34,72,-79,57,-25,-49,-89,70,-7,30,-61,-31,36,-98,15,-76,-8,20,5,
                       17,67,59,5,-6,-69,-36,8,87,-41,-29,23,4,51,84,67,86,-99,88,4,83,-97,-34,-52,49,-3,-47,82,
                       23,-41,-89,73,-75,17,-41,22,27,-7,22,14,84,-48,9,48,62,4,64,-24,81,-66,29,10,72,51,-9,-98,
                       -15,56,-41,-57,-26,86,71,-60,-17,38,-80,35,-98,78,17,-66,53,22,-58,63,-39,-39,24,26,-91,-53,
                       -44,-53,40,81,39,21,-100,-52,-55,-7,-95,-69,11,-25,-91,-37,33,8,88,-97,0,17,27,-90,15,-8,10,95,
                       38,-23,-65,-96],-207),
            expects = -207
        )
        self.push_test(
            params = ([-1, 2, 1, -4], 1),
            expects= 2

        )

    def solution(self, nums, target):
        nums = sorted(nums)
        length = len(nums)
        result = []
        for i in xrange(length):
            first = nums[i]
            left = i +1
            right = length -1
            if left >= right:
                break
            lastError = 10e9
            while True:
                if left >= right:
                    break
                current = first + nums[left] + nums[right]

                # optimization, if gradient start to increase, no need to search  (TO AVOID TLE)
                if abs(target- current) > lastError:
                    break
                else:
                    lastError= abs(target-current) # renew gradient

                if result == [] or abs(target- current) < abs( target - sum(result)):
                    result = [first, nums[left], nums[right]]

                # optimization: return when find optimal result (TO AVOID TLE)
                if current == target:
                    return target

                # step with least increase
                if abs(first + nums[left + 1] + nums[right] - target) < abs(first + nums[left] + nums[right -1] - target):
                    left = left + 1
                else:
                    right = right - 1

        closestsum = sum(result)
        return closestsum
