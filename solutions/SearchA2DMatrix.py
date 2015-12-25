from BaseSolution import *
class SearchA2DMatrix(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params =  ([  [1,1,1]], 1),
            expects = True
        )
        self.push_test(
            params =  ([  [1,   3,  5,  7],  [10, 11, 16, 20],[23, 30, 34, 50]], 11),
            expects = True
        )
    def solution(self, matrix, target):
        if not matrix or len(matrix) == 0: return False
        n, m = len(matrix), len(matrix[0])
        i = self.search([matrix[j][m-1] for j in range(n)], 0, n-1, target, t = 0)
        if i == -1: return False

        if self.search(matrix[i], 0, m-1, target, t = 2):
            return True
        else: return False

    def search(self, nums, left, right, target, t = 0):
        mid = (left+right)/2
        if left == right:
            if t==0:
                return left if nums[left] >= target else -1
            elif t ==1:
                return left if nums[left] <= target else -1
            else:
                return nums[left] == target
        elif target <= nums[mid]:
            return self.search(nums, left, mid, target, t)
        else:
            return self.search(nums, mid+1, right, target, t)