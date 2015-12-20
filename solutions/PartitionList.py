from BaseSolution import *
from ListNode import *
class PartitionList(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (ListNode.create_from_arr([1,4,3,2,5,2]),3),
            expects= ListNode.create_from_arr([1,2,2,4,3,5])
        )
        self.push_test(
            params = (ListNode.create_from_arr([]),0),
            expects= ListNode.create_from_arr([])
        )
    def solution(self, head, x):
        if head is None:
            return head
        nums = []
        top = head
        while top is not None:
            nums.append(top)
            top = top.next
        n = len(nums)
        small = [num for num in nums if num.val < x]
        big = [num for num in nums if num.val >= x]
        nums = small + big
        for i in range(0, n):
            if i < n-1:
                nums[i].next = nums[i+1]
            else:
                nums[i].next = None
        return nums[0]

    def solution(self, head, x):
        l = left = ListNode(-1)
        r = right = ListNode(-1)
        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                r.next = head
                r = r.next
            head = head.next
        r.next =None
        l.next = right.next
        newHead = left.next
        return newHead