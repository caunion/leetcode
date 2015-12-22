from BaseSolution import *
from ListNode import *
class LinkedListCycle(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, head):
        if not head: return False
        newHead = ListNode(-1)
        newHead.next = head
        slow = newHead
        fast = newHead.next
        while slow and fast and fast.next:
            if slow == fast: return True
            slow = slow.next
            fast = fast.next.next
        return False

