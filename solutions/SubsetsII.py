from BaseSolution import *
class SubsetsII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([5,5,5,5,5],),
            expects = [[],[5],[5,5],[5,5,5],[5,5,5,5],[5,5,5,5,5]]
        )
        self.push_test(
            params = ([0],),
            expects= [[],[0]]
        )
        self.push_test(
            params = ([1,2,2,3],),
            expects = [[],[3],[2],[2,3],[2,2],[2,2,3],[1],[1,3],[1,2],[1,2,3],[1,2,2],[1,2,2,3]],
            expect_unordered= True
        )
        self.push_test(
            params = ([0,0,1,2,2,3],),
            expects = [[],[3],[2],[2,3],[2,2],[2,2,3],[1],[1,3],[1,2],[1,2,3],[1,2,2],[1,2,2,3],[0],[0,3],
                       [0,2],[0,2,3],[0,2,2],[0,2,2,3],[0,1],[0,1,3],[0,1,2],[0,1,2,3],[0,1,2,2],[0,1,2,2,3],
                       [0,0],[0,0,3],[0,0,2],[0,0,2,3],[0,0,2,2],[0,0,2,2,3],[0,0,1],[0,0,1,3],[0,0,1,2],
                       [0,0,1,2,3],[0,0,1,2,2],[0,0,1,2,2,3]],
            expect_unordered= True
        )
    def solution(self, nums):
        if not nums or len(nums) == 0: return []
        n = len(nums)
        result = []
        nums = sorted(nums)
        # for i in range(0, n+1):
        #     for next in self.combination(nums, 0, n-1, i):
        #         result.append(next)
        self.result = result
        for i in range(0, n+1):
            self.recursiveComb(nums, 0, n-1, i, [])
        return self.result

    def combination(self, nums, left, right, count):
        if count == 0 or right- left + 1 < count:
            return
        elif right-left+1 == count:
            yield nums[left:right+1]
        else:
            j = left
            while j< len(nums)-1 and nums[j] == nums[j+1]: j+=1
            for i in range(left, j+1):
                if  count - (i -left + 1) >= 0:
                    for next in self.combination(nums, j+1, right, count - (i -left + 1) ):
                        if i+1-left + len(next) == count:
                            yield nums[left:i+1] + next
            for next in self.combination(nums, j+1, right, count):
                if len(next) == count:
                    yield next

    def recursiveComb(self, nums, left, right, count, prev):
        if count  < 0 or right -left + 1 < count:
            return
        elif count == 0:
            self.result.append(prev)
        elif right - left + 1 == count:
            prev.extend(nums[left: right+1])
            self.result.append(prev)
        else:
            j = left
            while j < len(nums) -1  and nums[j] == nums[j+1]: j+=1
            for i in range(left, j+1):
                if count - (i - left +1 ) >= 0:
                    next = prev + nums[left:i+1]
                    self.recursiveComb(nums, j+1, right, count - (i - left + 1), next)
            self.recursiveComb(nums, j+1, right, count, prev)

    def solution(self, nums):
        nums = sorted(nums)
        ret = []
        ret.append([])
        size = start = 0
        for i in xrange(len(nums)):
            start = size if i >= 1 and nums[i] == nums[i-1] else 0
            size = len(ret)
            for j in range(start, size):
                tmp = ret[j][:]
                tmp.append(nums[i])
                ret.append(tmp)

        return ret