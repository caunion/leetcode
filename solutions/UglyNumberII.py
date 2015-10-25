__author__ = 'Daoyuan'
from BaseSolution import *

class UglyNumberII(BaseSolution):
    """
    Write a program to find the n-th ugly number.Ugly numbers are positive numbers
    whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9,
    10, 12 is the sequence of the first 10 ugly numbers.

    https://leetcode.com/problems/ugly-number-ii/

    Medium, but tough for me
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.mark = True
        self.diff = 8
        self.push_test((2,),2)
        self.push_test((1,),1)
        self.push_test((9,), 10)
        self.push_test((10,), 12)

    def solution(self, n):
        ugly = [0] * (n+1)
        if n <= 0: return 0
        idx = 1
        ugly[1] = 1
        if n <= idx:
            return ugly[n]
        idx2 = idx3 = idx5 = 1
        while idx < n:
            next = min( ugly[idx2] * 2, ugly[idx3] * 3, ugly[idx5]*5)
            if next == ugly[idx2] * 2:
                idx2 = idx2 + 1
            if next == ugly[idx3] * 3:
                idx3 = idx3 + 1
            if next == ugly[idx5] * 5:
                idx5 = idx5 + 1
            idx = idx + 1
            ugly[idx] = next
        return ugly[n]

