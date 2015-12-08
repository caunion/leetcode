from BaseSolution import *
class MajorityElementII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params =([1,2,1,1,1,3,3,4,3,3,3,4,4,4],),
            expects = [3]
        )
    def solution(self, nums):
        inf = 1<<30
        if not nums or len(nums) == 0: return []
        if len(nums) == 1: return [nums[0]]
        cand1 = inf
        count1 = 0
        cand2 = inf
        count2 = 0
        for num in nums:
            if num == cand1 or num == cand2:
                if num == cand1: count1+=1
                else: count2 +=1
            elif cand1 == inf or cand2 == inf:
                if cand1 == inf:
                    cand1 = num
                    count1 = 1
                else:
                    cand2 = num
                    count2 = 1
            else:
                count1 -= 1
                count2 -= 1
                if count1 == 0:
                    cand1 = inf
                if count2 == 0:
                    cand2 = inf
        count1 = count2 = 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
        n = len(nums)
        result = []
        if count1 > n/3: result.append(cand1)
        if count2 > n/3: result.append(cand2)
        return result