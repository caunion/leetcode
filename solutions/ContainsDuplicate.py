__author__ = 'Daoyuan'
from BaseSolution import *
class ContainsDuplicate(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, nums):
        hash = set()
        for i in nums:
            if not hash.__contains__(i):
                hash.add(i)
            else:
                return True
        return False