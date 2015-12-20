from BaseSolution import *
from ListNode import *
class RotateList(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (ListNode.create_from_arr([]),0,),
            expects = ListNode.create_from_arr([])
        )
        self.push_test(
            params = (ListNode.create_from_arr([1,2,3,4,5]),2,),
            expects = ListNode.create_from_arr([4,5,1,2,3])
        )
        self.push_test(
            params = (ListNode.create_from_arr([1,2,3,4,5]),17,),
            expects = ListNode.create_from_arr([4,5,1,2,3])
        )
    def solution(self, head, k):
        if k==0 or head is None: return head
        queue = []
        count = 0
        top = head
        while top is not None:
            if count > k:
                queue.pop(0)
            queue.append(top)
            count += 1
            top = top.next
        k = k % count
        newHead = queue[-k]
        queue[-1].next = head
        queue[-k-1].next = None
        return newHead