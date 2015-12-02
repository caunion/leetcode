__author__ = 'Daoyuan'
from BaseSolution import *

class LongestIncreasingSubsequence(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ([10, 9, 2, 5, 3, 7, 101, 18],),
            expects = 4
        )
    def solution(self, nums):
        if not nums or nums == []: return 0
        n = len(nums)
        buf = [nums[0]]
        for i in range(1, n):
            num = nums[i]
            j = self.binSearch(buf, num, 0, len(buf) -1)
            if j < len(buf):
                buf[j] = num
            else:
                buf.append(num)

        return len(buf)


    def binSearch(self, lis, val, left, right):
        if left > right:
            return -1
        elif left == right:
            if lis[left] < val:
                return left + 1
            else:
                return left
        else:
            mid = (left + right) / 2
            if lis[mid] >= val:
                return  self.binSearch(lis, val, left, mid)
            elif lis[mid+1] < val:
                return self.binSearch(lis, val, mid+1, right)
            elif lis[mid] < val <= lis[mid+1] :
                return mid+1
