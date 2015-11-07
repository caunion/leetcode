__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
from ListNode import *
class ConvertSortedListToBinarySearchTree(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (ListNode.create_from_arr([1,2,3,4,5,6,7]),),
            expects = TreeNode.deserialize("{4,2,6,1,3,5,7}")
        )

    def solution(self, head):
        arr = []
        top = head
        while top:
            arr.append(top.val)
            top = top.next
        tree = self.buidTree(arr, 0, len(arr))
        return tree

    def buidTree(self,arr,left, right):
        if left == right: return None
        mid = (left + right) / 2
        root = TreeNode(arr[ mid ])
        root.left = self.buidTree(arr, left, mid)
        root.right = self.buidTree(arr, mid+1, right)
        return root