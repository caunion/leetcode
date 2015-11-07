__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
from ListNode import *
class ConvertSortedArrayToBinarySearchTree(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([1,2,3,4,5,6,7],),
            expects = TreeNode.deserialize("{4,2,6,1,3,5,7}")
        )

    def solution(self,nums):
        return self.buildTree(nums, 0, len(nums))

    def buildTree(self, nums, left, right):
        if right == left: return None
        mid = (left+right)/2
        root = TreeNode(nums[mid])
        root.left = self.buildTree(nums,left, mid)
        root.right = self.buildTree(nums,mid+1, right)
        return root