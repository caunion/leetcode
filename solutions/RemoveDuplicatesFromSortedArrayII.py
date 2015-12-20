from BaseSolution import *
class RemoveDuplicatesFromSortedArrayII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,2,2,2,1,1,3,3,1,1,1,3],),
            expects = [1,2,2,1,1,3,3,1,1,3]
        )
        self.push_test(
            params = ([-3,-1,-1],),
            expects = [-3,-1,-1]
        )
    def solution(self, nums):
        end = self.removeDuplicates(nums)
        ret = nums[0:end]
        return ret
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=0
        fast=1
        count = 1
        nums.append(-1<<30)
        n = len(nums)
        while slow < n and fast < n:
            if nums[fast] == nums[fast-1]:
                count += 1
                if count < 3:
                    nums[slow+1] = nums[fast]
                    slow += 1
                    fast += 1
                else:
                    fast += 1
            else:
                count = 1
                nums[slow+1] = nums[fast]
                slow += 1
                fast += 1
        return slow