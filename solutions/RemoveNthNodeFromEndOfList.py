from BaseSolution import *
from ListNode import *
class RemoveNthNodeFromEndOfList(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (ListNode.create_from_arr([1]),1),
            expects= ListNode.create_from_arr([])
        )
        self.push_test(
            params = (ListNode.create_from_arr([1,2,3,4]),4),
            expects= ListNode.create_from_arr([2,3,4])
        )
    def solution(self, head, n):
        if not head: return None
        newhead = ListNode(0)
        newhead.next = head
        queue = []
        count = 0
        top = newhead
        while top is not None:
            if count > n + 2:
                queue.pop(0)
            queue.append(top)
            top = top.next
            count += 1
        if n == 1:
            queue[-n-1].next = None
        else:
            queue[-n-1].next = queue[-n+1]
        return newhead.next