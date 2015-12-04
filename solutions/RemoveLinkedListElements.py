__author__ = 'Daoyuan'
from BaseSolution import *
from ListNode import *
class RemoveLinkedListElements(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (ListNode.create_from_arr([1,2]),0),

        )
    def solution(self, head, val):
        if not head: return head
        top = ListNode(0)
        top.next = head
        prev = head = top
        while top:
            if top.val == val:
                if top.next:
                    top.val = top.next.val
                    top.next = top.next.next
                else:
                    prev.next = None
                    break
            else:
                prev = top
                top = top.next
        return head.next