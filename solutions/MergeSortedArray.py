__author__ = 'Caunion'
from BaseSolution import *

class MergeSortedArray(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (
                [2,0],
                1,
                [1],
                1
            ),
            expects = [1,2]
        )
        self.push_test(
            params = (
                [0],
                0,
                [1],
                1
            ),
            expects = [1]
        )
        self.push_test(
            params = (
                [],
                0,
                range(0,10),
                10
            ),
            expects = range(0,10)
        )
        self.push_test(
            params = (
                [],
                0,
                [],
                0
            ),
            expects = []
        )
        self.push_test(
            params = (
                    [1],
                    1,
                    [],
                    0),
            expects = [1]
        )
        self.push_test(
            params = (
                range(0,10),
                10,
                [],
                0
            ),
            expects =  range(0,10)
        )

    def solution(self, nums1, m, nums2, n):
        self.merge_return(nums1, m, nums2, n)
        return nums1

    def merge_return(self,nums1, m, nums2, n):
        if m == 0:
            del nums1[:]
            nums1[:] = nums2[:]
            return
        if n == 0:
            return
        i = 0
        j = 0
        del nums1[m:]
        del nums2[n:]
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i,nums2[j])
                j=j+1
                i = i + 1
                m = m + 1
            else:
                i = i+1
        if j<n:
            nums1[i:] = nums2[j:]
        return