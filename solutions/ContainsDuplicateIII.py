__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *

class ContainsDuplicateIII(BaseSolution):
    """
    distinct indices i and j in the array such that the
    difference between nums[i] and nums[j] is at most t
    and the difference between i and j is at most k.
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([0, 4, 7, 10,15, 20, 7, 25,  30, 9, 35,40], 3, 2),
            expects = True
        )
        self.push_test(
            params = ([1,3,5,7,9,10,11,13], 3,1),
            expects = True
        )

    def solution(self, nums, k, t):
        if not nums or len(nums) == 0: return False
        root = TreeNode(nums[0])
        root.state = 0
        n = len( nums )
        self.k = k
        self.t = t
        for i in range(1, n):
            num = nums[i]
            node = TreeNode(num)
            node.state = i
            if self.find(root,i, num-t, num+t):
                return True
            self.insert(root, node)
        return False

    def insert(self, root, node):
        if not root: return
        if root.val < node.val:
            if root.right:
                self.insert(root.right, node)
            else:
                root.right = node
        elif root.val > node.val:
            if root.left:
                self.insert(root.left, node)
            else:
                root.left = node
        else:
            root.state = node.state

    def find(self, root, time, left, right):
        if not root: return False
        elif left <= root.val <= right:
            if time - root.state <= self.k:
                return True
            else:
                return self.find(root.left, time, left, root.val) or \
                        self.find(root.right, time, root.val, right)
        elif right < root.val:
            return self.find(root.left, time, left, right)
        else:
            return self.find(root.right, time, left, right)


# class TreeNode(object):
#     def __init__(self, val= -1, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = None
#         self.parent = None
#
#         #for traverse
#         self.state = -1
#         #for disjoint set
#         self.rank = -1
#         # for multi-branch tree
#         self.children = []